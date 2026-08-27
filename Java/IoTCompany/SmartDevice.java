package IoTCompany;

public abstract class SmartDevice implements DeviceInterface{
    protected String deviceId, name;
    protected Status powerStatus;
    protected double powerUsage;

    public SmartDevice(String deviceId, String name, Status powerStatus, double powerUsage) {
        this.deviceId = deviceId;
        this.name = name;
        this.powerStatus = powerStatus;
        this.powerUsage = powerUsage;
    }
    public SmartDevice() {
        deviceId = null;
        name = null;
        powerStatus = null;
        powerUsage = 0;
    }

    @Override
    public void turnOn(String userId) {
        powerStatus = Status.ON;
    }

    @Override
    public void turnOff(String userId) {
        powerStatus = Status.OFF;
    }

    @Override
    public String getPowerStatus() {
        return " "+ powerStatus;
    }
}
