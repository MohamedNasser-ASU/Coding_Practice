package MarketPlace;

public class Main {

    public static void main(String[] args){

        Product laptop = new Product("P1", "laptop", 1500, 12);
        Service techSupport = new Service("S1", "tech", 150, 2);
        Customer customer = new Customer("Mohamed" ,3000 ,Role.SHOPPER);
        try{
            System.out.println("Attempting to buy service as SHOPPER...");
            customer.purchaseService(techSupport);
        }
        catch (InvalidPurchaseException e){
            System.out.println("Exception caught: " + e.getMessage());
        }
        customer.setRole(Role.BUSINESS_BUYER);
        try{
            System.out.println("Attempting to buy service as Business Buyer...");
            customer.purchaseService(techSupport);
        }
        catch (InvalidPurchaseException e){
            System.out.println("Exception caught: " + e.getMessage());
        }


    }

}
