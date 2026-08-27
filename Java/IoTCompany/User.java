package IoTCompany;

public class User {
    private static int idCount = 1;
    private int id;
    private String name;
    Role role;

    public User(String name, Role role) {
        id = idCount++;
        this.name = name;
        this.role = role;
    }

    public void toggleLight(SmartLight light){
        if ( light.powerStatus == Status.OFF ){
            light.powerStatus = Status.ON;
        }
        else {
            light.powerStatus = Status.OFF;
        }
    }

    public void adjustThermostat(Thermostat thermostat) throws PermissionDeniedException{
        if (this.role == Role.CHILD){
            throw new PermissionDeniedException("A child can't adjust thermostat");
        }
        if ( thermostat.powerStatus == Status.OFF ){
            thermostat.powerStatus = Status.ON;
        }
        else {
            thermostat.powerStatus = Status.OFF;
        }

    }
}
