package PaymentSystem;

abstract class Payment {

    protected final String transactionId;
    protected double amount;

    public Payment(String transactionId, double amount) {
        this.transactionId = transactionId;
        this.amount = amount;
    }

    abstract void validatePayment();

    public final void printReceipt() {
        System.out.println("Transaction ID: " + transactionId);
        System.out.println("Amount: " + amount);
    }
}