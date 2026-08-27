package IoTCompany;

public class SmartLight extends SmartDevice{
    private int brightnessLevel;

    public SmartLight(String deviceId, String name, Status powerStatus, double powerUsage, int brightnessLevel) {
        super(deviceId, name, powerStatus, powerUsage);
        this.brightnessLevel = brightnessLevel;
    }
    public SmartLight() {
        super();
        brightnessLevel =50;
    }

    @Override
    public String toString() {
        return "SmartLight{" +
                "brightnessLevel=" + brightnessLevel +
                ", deviceId='" + deviceId + '\'' +
                ", name='" + name + '\'' +
                ", powerStatus=" + powerStatus +
                ", powerUsage=" + powerUsage +
                '}';
    }
}
