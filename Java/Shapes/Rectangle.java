package Shapes;

import java.io.IOException;

public class Rectangle extends Shape{
    private double length, width;

    public Rectangle(int length, int width) throws IOException {

            if (length <= 0 || width <=0 ){
                throw new IOException("Error: wrong data");
            }
            else{
                this.length = length;
                this.width = width;
            }

    }

    @Override
    public double getArea(){
        return this.length*this.width;
    }

    public String printData(){
        return "Rectangle data. length: " + this.length + " width: " + this.width +" area: " + String.valueOf(getArea());
    }

    @Override
    public void increment(){
        this.length++;
        this.width++;
    }
}
