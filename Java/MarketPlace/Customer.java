package MarketPlace;

public class Customer {

    private static int idCount = 1;
    int id;
    String name;
    double balance;
    private Role role;

    public Customer( String name, double balance, Role role) {

        this.id = idCount++;
        this.name = name;
        this.balance = balance;
        this.role = role;
    }

    public void purchaseProduct(Product product) {

        product.purchaseItem(String.valueOf(id));
        balance -= product.price;
        System.out.println(name + " successfully purchased " + product.name);
    }

    public void returnProduct(Product product) {

        product.returnItem(String.valueOf(id));
        balance += product.price;
        System.out.println(name + " successfully returned " + product.name);

    }

    public void purchaseService(Service service) {

        if (role == Role.SHOPPER) {
            throw new InvalidPurchaseException("shopper can't buy service");
        } else {
            service.purchaseItem(String.valueOf(id));
            balance -= service.price;
            System.out.println(name + " successfully booked " + service.name);
        }

    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }


}
