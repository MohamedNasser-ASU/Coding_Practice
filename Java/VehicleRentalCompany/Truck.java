package VehicleRentalCompany;

public class Truck extends Vehicle{
    private int payloadCapacity;

    public Truck(String vehicleId, String model, String condition, double dailyRate, int payloadCapacity) {
        super(vehicleId, model, condition, dailyRate);
        this.payloadCapacity = payloadCapacity;
    }

    public Truck() {
        super();
        payloadCapacity = 1000;
    }

    @Override
    public String toString() {
        return "Truck{" +
                "payloadCapacity=" + payloadCapacity +
                ", vehicleId='" + vehicleId + '\'' +
                ", model='" + model + '\'' +
                ", condition='" + condition + '\'' +
                ", dailyRate=" + dailyRate +
                '}';
    }

}
