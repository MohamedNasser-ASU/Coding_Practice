package PaymentSystem;

public class Main{
    public static void main(String[] args){
        Payment credit = new CreditCardPayment("transaction1", 100, "1234567812345678");
        Payment paypal = new PayPalPayment("transaction2" , 200 , "mohamed@gmail.com");
        credit.validatePayment();
        ((Payable)credit).pay(100);
        credit.printReceipt();
        paypal.validatePayment();
        ((Payable)paypal).pay(200);
        paypal.printReceipt();


    }
}