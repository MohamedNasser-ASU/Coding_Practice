package MarketPlace;

public abstract class MarketplaceItem implements MarketplaceItemInterface {
    protected String itemID;
    protected String name;
    protected double price;
    protected String status;

    public MarketplaceItem( String itemID , String name, double price){
        this.itemID = itemID;
        this.name = name;
        this.price = price;
        this.status ="Available";
    }

    protected MarketplaceItem() {
    }


    public void purchaseItem(String customerId) {
        this.status = "purchased";
    }

    public void returnItem(String customerId) {
        this.status = "available";
    }

    public String getItemStatus() {
        return this.status;
    }

}
