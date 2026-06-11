package Bank;

public class BasicSaving extends SavingAccount {

    public BasicSaving() {
        this.setInterestRate(0.05);
    }

    public BasicSaving(int id, double balance, double interestRate) {
        super(id, balance, interestRate);
        this.setInterestRate(0.05);
    }

}
