package PaymentSystem;

class CreditCardPayment extends Payment implements Payable {
    private String cardNumber;
    public CreditCardPayment(String transactionId, double amount, String cardNumber) {
        super(transactionId, amount);
        this.cardNumber = cardNumber;
    }
    @Override
    void validatePayment() {
        if (cardNumber.length() == 16) {
            System.out.println("Credit Card validated.");
        } else {
            System.out.println("Invalid Credit Card.");
        }
    }
    @Override
    public void pay(double amount) {
        System.out.println("Paid " + amount + " using Credit Card.");
    }
}
