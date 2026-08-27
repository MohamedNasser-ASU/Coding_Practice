package VehicleRentalCompany;

public abstract class Vehicle implements RentableInterface{

    protected String vehicleId, model, condition;
    protected double dailyRate;

    public Vehicle(String vehicleId, String model, String condition, double dailyRate) {
        this.vehicleId = vehicleId;
        this.model = model;
        this.condition = condition;
        this.dailyRate = dailyRate;
    }

    public Vehicle() {
        condition = "available";
    }
    @Override
    public void rentVehicle(String driverId){
        this.condition = "rented";
    }

    @Override
    public void returnVehicle(String driverId){
        this.condition = "available";
    }

    @Override
    public String getVehicleCondition(){
        return condition;
    }
}
