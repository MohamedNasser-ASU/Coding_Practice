package MarketPlace;

public class Service extends MarketplaceItem{
    int duration;

    public Service(int duration) {
        this.duration = 1;
    }

    public Service(String itemID, String name, double price, int duration) {
        super(itemID, name, price);
        this.duration = duration;
    }

    @Override
    public String toString() {
        return "Product [ID: " + itemID + ", Name: " + name + ", Price: $" + price + ", Warranty: " + duration + " hours]";
    }

}
