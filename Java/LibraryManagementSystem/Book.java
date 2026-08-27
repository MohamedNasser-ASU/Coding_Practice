package LibraryManagementSystem;

public class Book extends LibraryItem{

    int pageCount;

    /// default
    public Book(){
        super();
        pageCount = 300;
    }

    /// parameterized
    public Book(String itemID, String title, String status, double replacementCost, int pageCount) {
        super(itemID, title, status, replacementCost);
        this.pageCount = pageCount;
    }

    @Override
    public String toString() {
        return "Book{" +
                "pageCount=" + pageCount +
                ", itemID='" + itemID + '\'' +
                ", title='" + title + '\'' +
                ", status='" + status + '\'' +
                ", replacementCost=" + replacementCost +
                '}';
    }

}
