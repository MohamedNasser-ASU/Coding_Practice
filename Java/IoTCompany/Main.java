package IoTCompany;

public class Main {
    public static void main(String[] args) {
        SmartLight light1 = new SmartLight("l1", "lighttt", Status.OFF, 130, 69);
        Thermostat thermo1 = new Thermostat("t1", "thermooo", Status.OFF, 130, 100);
        User user1 = new User("Mohamed", Role.CHILD);
        System.out.println("Attempting adjustment by child");
        try {
            user1.adjustThermostat(thermo1);
        } catch (PermissionDeniedException e) {
            System.out.println("Error :" + e.getMessage());
        }
        user1.role = Role.ADMIN;
        System.out.println("Attempting adjustment by Admin");
        try {
            System.out.println(thermo1.powerStatus);
            user1.adjustThermostat(thermo1);
            System.out.println(thermo1.powerStatus);
        } catch (PermissionDeniedException e) {
            System.out.println("Error :" + e.getMessage());
        }


    }
}

