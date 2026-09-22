import pytest
import project


def test_parse_record():
    record, state, reason = project.parse_record(
        "500 INFO TEMP_C=31.2 SUPPLY_V=5.98 RPM_L=132 RPM_R=126 "
        "CMD_L=35 CMD_R=35 THROTTLE=35 STEER=0"
    )

    assert state == "ok"
    assert record["timestamp"] == 500
    assert record["temp_c"] == 31.2
    assert record["rpm_l"] == 132

    record, state, reason = project.parse_record(
        "22000 INFO TEMP_C=86.0 SUPPLY_V=5.72 RPM_L=248 RPM_R=0 "
        "CMD_L=70 CMD_R=70 THROTTLE=70"
    )

    assert state == "malformed"
    assert reason == "Missing telemetry"

    record, state, reason = project.parse_record("THIS IS NOT A LOG LINE")

    assert record is None
    assert state == "malformed"


def test_load_log(tmp_path):
    logfile = tmp_path / "test.log"

    logfile.write_text(
        "0 INFO EVENT=SESSION_START PPR=20 WHEEL_MM=65 NOMINAL_V=6.0\n"
        "500 INFO TEMP_C=31.2 SUPPLY_V=5.98 RPM_L=132 RPM_R=126 "
        "CMD_L=35 CMD_R=35 THROTTLE=35 STEER=0\n"
        "1000 INFO TEMP_C=abc SUPPLY_V=5.90 RPM_L=140 RPM_R=138 "
        "CMD_L=40 CMD_R=40 THROTTLE=40 STEER=0\n"
        "1500 INFO TEMP_C=32.0 SUPPLY_V=5.95 RPM_L=150 RPM_R=148 "
        "CMD_L=40 CMD_R=40 THROTTLE=40 STEER=0\n"
    )

    records, malformed = project.load_log(logfile)

    assert len(records) == 3
    assert len(malformed) == 1
    assert malformed[0][0] == 3
    assert malformed[0][1] == "Invalid value"


def test_get_stats():
    stats = project.get_stats([10, 20, 30, 40])

    assert stats[0] == 10
    assert stats[1] == 40
    assert stats[2] == 25


def test_analyze_records():
    records = [
        {
            "timestamp": 0,
            "level": "INFO",
            "event": "SESSION_START",
            "ppr": 20,
            "wheel_mm": 65,
            "nominal_v": 6.0
        },
        {
            "timestamp": 500,
            "level": "INFO",
            "temp_c": 30.0,
            "supply_v": 6.0,
            "rpm_l": 100,
            "rpm_r": 100,
            "cmd_l": 30,
            "cmd_r": 30,
            "throttle": 30,
            "steer": 0
        },
        {
            "timestamp": 1000,
            "level": "INFO",
            "temp_c": 40.0,
            "supply_v": 5.8,
            "rpm_l": 200,
            "rpm_r": 200,
            "cmd_l": 60,
            "cmd_r": 60,
            "throttle": 60,
            "steer": 10
        }
    ]

    stats = project.analyze_records(records)

    assert stats["temps"] == (30.0, 40.0, 35.0)
    assert stats["volts"] == (5.8, 6.0, 5.9)
    assert stats["rpml"] == (100, 200, 150)
    assert stats["rpmr"] == (100, 200, 150)

    assert stats["velocity"][0] == pytest.approx(1.225, abs=0.01)
    assert stats["velocity"][1] == pytest.approx(2.450, abs=0.01)


def test_detect_anomalies():
    record = {
        "temp_c": 85.0,
        "supply_v": 5.2,
        "rpm_l": 250,
        "rpm_r": 150,
        "cmd_l": 70,
        "cmd_r": 70,
        "throttle": 70,
        "steer": 0
    }

    anomalies = project.detect_anomalies(record)

    assert "high_temperature" in anomalies
    assert "low_supply" in anomalies
    assert "motor_mismatch" in anomalies

    normal = {
        "temp_c": 40.0,
        "supply_v": 5.9,
        "rpm_l": 180,
        "rpm_r": 175,
        "cmd_l": 50,
        "cmd_r": 50,
        "throttle": 50,
        "steer": 0
    }

    assert project.detect_anomalies(normal) == []


def test_log_events():
    records = [
        {
            "timestamp": 1000,
            "level": "WARN",
            "event": "HIGH_TEMPERATURE",
            "temp_c": 82.0
        },
        {
            "timestamp": 2000,
            "level": "WARN",
            "event": "LOW_SUPPLY",
            "supply_v": 5.3
        },
        {
            "timestamp": 3000,
            "level": "WARN",
            "event": "MOTOR_SPEED_MISMATCH",
            "rpm_l": 250,
            "rpm_r": 160,
            "cmd_l": 70,
            "cmd_r": 70
        },
        {
            "timestamp": 4000,
            "level": "ERROR",
            "event": "MOTOR_STALL",
            "side": "RIGHT",
            "rpm_r": 0,
            "cmd_r": 75
        }
    ]

    events = project.log_events(records)

    assert events["warnings"] == 3
    assert events["errors"] == 1
    assert events["high_temperature"] == 1
    assert events["low_supply"] == 1
    assert events["motor_mismatch"] == 1
    assert events["motor_stall"] == 1
