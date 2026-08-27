package VehicleRentalCompany;

public interface RentableInterface {
    void rentVehicle(String driverId);
    void returnVehicle(String driverId);
    String getVehicleCondition();
}
