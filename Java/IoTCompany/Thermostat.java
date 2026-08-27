package IoTCompany;

public class Thermostat extends SmartDevice{
    private int targetTemperature;

    public Thermostat(String deviceId, String name, Status powerStatus, double powerUsage, int targetTemperature) {
        super(deviceId, name, powerStatus, powerUsage);
        this.targetTemperature = targetTemperature;
    }
    public Thermostat() {
        super();
        targetTemperature = 22;


    }

    @Override
    public String toString() {
        return "Thermostat{" +
                "targetTemperature=" + targetTemperature +
                ", deviceId='" + deviceId + '\'' +
                ", name='" + name + '\'' +
                ", powerStatus=" + powerStatus +
                ", powerUsage=" + powerUsage +
                '}';
    }
}
