package MarketPlace;

public interface MarketplaceItemInterface {
    void purchaseItem(String customerId);
    void returnItem(String customerId);
    String getItemStatus();
}
