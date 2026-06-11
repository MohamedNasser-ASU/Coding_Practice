package Shapes;

import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        Shape[] shapes = new Shape[3];
        try {

            shapes[0] = new Rectangle(10, 5);
            shapes[1] = new Square(3);
            shapes[2] = new Triangle(2, 4);

            System.out.println("before sort");
            for (int i =0; i<=2; i++){
                System.out.println(shapes[i].printData());
            }

            Arrays.sort(shapes);

            System.out.println("after sort");
            for (int i =0; i<=2; i++){
                System.out.println(shapes[i].printData());
            }

            System.out.println("Comparing");
            System.out.println(shapes[0].equals(shapes[1]));

            Thread t1 = new Thread(shapes[0]);
            Thread t2 = new Thread(shapes[1]);
            Thread t3 = new Thread(shapes[2]);

            System.out.println("after inc");

            t1.start();
            t2.start();
            t3.start();

            t1.join();
            t2.join();
            t3.join();

            for (int i =0; i<=2; i++){
                System.out.println(shapes[i].printData());
            }

        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
        catch (InterruptedException e){
            System.out.println(e.getMessage());
        }


    }
}
