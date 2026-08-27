package Shapes;

import java.io.IOException;

public class Triangle extends Shape{

    private double base ,height;

    public Triangle() {
    }

    public Triangle(double base, double height) throws IOException {
        if (base <= 0 || height <=0 ){
            throw new IOException("Error: wrong data");
        }
        else{
            this.base = base;
            this.height = height;
        }
    }

    @Override
    public double getArea(){
        return this.base*this.height*0.5;
    }

    public String printData(){
        return "Triangle data. height: " + this.height + " base: " + this.base +" area: " + String.valueOf(getArea());
    }

    @Override
    public void increment(){
        this.base++;
        this.height++;
    }
}
