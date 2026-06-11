package Bank;

public class Main {
        public static void main (String[] args){

        Account s1 = new BasicSaving(100,1000,5);
        SavingAccount s2 = new PremiumSaving(200,1000,5);
        Account c1 = new CheckingAccount(1,1000);

        System.out.println(((BasicSaving)s1).getInterestRate());
        System.out.println(s2.getInterestRate());
        c1.withdraw(300);
        s1.deposit(300);
        System.out.println(c1.getBalance());
        System.out.println(s1.getBalance());
        ((BasicSaving)s1).addInterest();
        System.out.println(s1.getBalance());

    }
}
