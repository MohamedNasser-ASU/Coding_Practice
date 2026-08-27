package VehicleRentalCompany;

public class Car extends Vehicle{
    private int seatingCapacity;

    public Car() {
        super();
        this.seatingCapacity = 5;
    }

    public Car(String vehicleId, String model, String condition, double dailyRate, int seatingCapacity) {
        super(vehicleId, model, condition, dailyRate);
        this.seatingCapacity = seatingCapacity;
    }

    @Override
    public String toString() {
        return "Car{" +
                ", vehicleId='" + vehicleId + '\'' +
                ", model='" + model + '\'' +
                "seatingCapacity=" + seatingCapacity +
                ", condition='" + condition + '\'' +
                ", dailyRate=" + dailyRate +
                '}';
    }
}
