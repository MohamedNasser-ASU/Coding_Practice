import pytest
from datetime import date, timedelta
from seasons import getBd, returnMin


def test_getBd():
    assert getBd("2007-06-11") == date(2007, 6, 11)
    assert getBd("2000-01-01") == date(2000, 1, 1)
    assert getBd("2024-02-29") == date(2024, 2, 29)


def test_getBd_invalid():
    with pytest.raises(SystemExit):
        getBd("June 11, 2007")

    with pytest.raises(SystemExit):
        getBd("2007-13-11")

    with pytest.raises(SystemExit):
        getBd("2007-02-30")


def test_returnMin_today():
    today = date.today()
    assert returnMin(today) == "Zero minutes"


def test_returnMin_one_day():
    yesterday = date.today() - timedelta(days=1)
    assert returnMin(yesterday) == "One thousand, four hundred forty minutes"


def test_returnMin_two_days():
    two_days_ago = date.today() - timedelta(days=2)
    assert returnMin(two_days_ago) == "Two thousand, eight hundred eighty minutes"
