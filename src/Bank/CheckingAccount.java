package Bank;

public class CheckingAccount extends Account {

    public CheckingAccount() {
    }

    public CheckingAccount(int id, double balance) {
        super(id, balance);
    }

    @Override
    public void withdraw(double amount){
        if ( amount >0 && amount <= this.getBalance())
            setBalance(getBalance()-amount);
    }

    @Override
    public String toString() {
        return "CheckingAccount{}";
    }
}
