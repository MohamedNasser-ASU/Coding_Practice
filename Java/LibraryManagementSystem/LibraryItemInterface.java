package LibraryManagementSystem;

public interface LibraryItemInterface {

    void borrowItem(String memberId);
    void returnItem(String memberId);
    String getItemStatus();

}
