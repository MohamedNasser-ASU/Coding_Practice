package Bank;

public class Account {
    private int id;
    private double balance;

    public Account(){
        this.id = 0;
        this.balance = 0.0;
    }
    public Account(int id, double balance) {
        this.id = id;
        this.balance = balance;
    }
    public void setId(int id) {
        this.id = id;
    }
    public void setBalance(double balance) {
        this.balance = balance;
    }
    public int getId() {
        return id;
    }
    public double getBalance() {
        return balance;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", balance=" + balance +
                '}';
    }

    public void withdraw(double amount){}
    public void deposit(double amount){
        this.balance += amount;
    }
}
