package IoTCompany;

public interface DeviceInterface {
    void turnOn(String userId);
    void turnOff(String userId);
    String getPowerStatus();
}
