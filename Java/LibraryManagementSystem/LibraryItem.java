package LibraryManagementSystem;

public abstract class LibraryItem implements LibraryItemInterface{

    protected String itemID, title, status;
    protected double replacementCost;

    //parameterized
    public LibraryItem(String itemID, String title, String status, double replacementCost) {
        this.itemID = itemID;
        this.title = title;
        this.status = status;
        this.replacementCost = replacementCost;
    }

    //no arg
    public LibraryItem() {
        status = "Available";
    }

    @Override
    public void borrowItem(String memberId) {
        this.status ="borrowed";
    }
    @Override
    public void returnItem(String memberId) {
        this.status ="Available";

    }
    @Override
    public String getItemStatus() {
        return this.status;
    }
}
