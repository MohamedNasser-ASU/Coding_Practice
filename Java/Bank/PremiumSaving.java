package Bank;

public class PremiumSaving extends SavingAccount{

    public PremiumSaving() {
        this.setInterestRate(0.1);
    }

    public PremiumSaving(int id, double balance, double interestRate) {
        super(id, balance, interestRate);
        this.setInterestRate(0.1);
    }

}
