package Bank;

public class SavingAccount extends Account{
    private double interestRate;

    public SavingAccount(){

    }

    public SavingAccount(int id, double balance, double interestRate) {
        super(id, balance);
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate;
    }
    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }

    @Override
    public void withdraw(double amount) {
        if (this.getBalance() > 500) {
            if (amount > 0) {
                setBalance(getBalance() - amount);
            }
        } else return;
    }
    public void addInterest(){
        setBalance(getBalance()*(1+this.interestRate));
    }

    @Override
    public String toString() {
        return "SavingAccount{" +
                "interestRate=" + interestRate +
                '}';
    }
}
