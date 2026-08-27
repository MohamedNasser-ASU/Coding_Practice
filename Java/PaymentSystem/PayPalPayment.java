package PaymentSystem;

class PayPalPayment extends Payment implements Payable {

    public String email;

    public PayPalPayment ( String transactionID , double amount ,String email){
        super(transactionID , amount);
        this.email = email;
    }

    @Override
    public void pay(double amount) {
        System.out.println("payed with PayPal");
    }

    @Override
    void validatePayment() {

        if (email.contains("@")) {
            System.out.println("PayPal account validated.");
        } else {
            System.out.println("Invalid PayPal email.");
        }

    }
}
