package LibraryManagementSystem;

public class Magazine extends LibraryItem {

    int issueNumber;

    //default
    public Magazine(){
        super();
        issueNumber = 1;
    }

    //parameterized
    public Magazine(String itemID, String title, String status, double replacementCost, int issueNumber) {
        super(itemID, title, status, replacementCost);
        this.issueNumber = issueNumber;
    }

    @Override
    public String toString() {
        return "Magazine{" +
                "issueNumber=" + issueNumber +
                ", itemID='" + itemID + '\'' +
                ", title='" + title + '\'' +
                ", status='" + status + '\'' +
                ", replacementCost=" + replacementCost +
                '}';
    }

}
