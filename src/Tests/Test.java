package Tests;

public class Test {
    int x =1;
}
class test2 extends Test {
    public test2 (int x)
    {
        super.x = x;
    }

    public static void main (String[] args){
        test2 t = new test2(10);
        System.out.println(t.x);
    }
}
