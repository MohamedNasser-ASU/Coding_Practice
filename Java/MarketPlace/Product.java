package MarketPlace;

public class Product extends MarketplaceItem {
    int warrantyPeriod;

    public Product(){
        super();
        this.warrantyPeriod = 12;
    }

    public Product(String itemID, String name, double price , int warrantyPeriod){
        super(itemID ,name, price);
        this.warrantyPeriod = 12;
    }

    @Override
    public String toString() {
        return "Product [ID: " + itemID + ", Name: " + name + ", Price: $" + price + ", Warranty: " + warrantyPeriod + " months]";
    }
}
