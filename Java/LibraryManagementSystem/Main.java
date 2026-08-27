package LibraryManagementSystem;

public class Main {
    public static void main(String[] args) {
        LibraryItem book1 = new Book("b1", "Awlad_7aretna", "Available", 300, 300);
        LibraryItem magazine1 = new Magazine("m1", "niceMagazine", "Available", 300, 3);
        Member member1 = new Member("Mohamed", 3000, Role.JUNIOR);

        System.out.println("Attempting to borrow magazine as JUNIOR...");
        try {
            member1.borrowMagazine((Magazine)magazine1);
        } catch (AgeRestrictionException e) {
            System.out.println("Exception: " + e.getMessage());
        }
        System.out.println("\n-------------------------\n");
        System.out.println("Changing role to ADULT...");
        member1.role = Role.ADULT;
        try {
            member1.borrowMagazine((Magazine)magazine1);
        } catch (AgeRestrictionException e) {
            System.out.println("Exception " + e.getMessage());
        }

    }
}
