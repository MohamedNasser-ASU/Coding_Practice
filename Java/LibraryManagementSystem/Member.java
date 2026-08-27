package LibraryManagementSystem;

public class Member {
    private int id;
    private String name;
    private double fineBalance;
    private static int idCount = 1;
    Role role;

    /// constructor
    public Member(String name, double fineBalance, Role role){
        this.id = idCount++;
        this.name = name;
        this.fineBalance = fineBalance;
        this.role = role;
    }

    /// setters and getters

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public double getFineBalance() {
        return fineBalance;
    }
    public void setFineBalance(double fineBalance) {
        this.fineBalance = fineBalance;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this . id = id;
    }

    void borrowBook(Book book) {
        if (book.status.equals("Available")) {
            book.borrowItem(String.valueOf(this.id));
            System.out.println("Borrowed book:" + book.title);
        } else {
            System.out.println("Sorry, " + book.title + " is currently borrowed.");
        }
    }

    void borrowMagazine(Magazine magazine) throws AgeRestrictionException{

        if (this.role == Role.JUNIOR) {
            throw new AgeRestrictionException("Juniors can't borrow magazines");
        }

        if (magazine.status.equals("Available")) {
            magazine.borrowItem(String.valueOf(this.id));
            System.out.println("Borrowed Magazine:" + magazine.title);
        }
        else {System.out.println("Sorry, " + magazine.title + " is currently borrowed.");}
    }

}
