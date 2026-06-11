package Shapes;

import java.io.IOException;

public class Square extends Shape{
    private double side;

    public Square(int side) throws IOException{
        if (side <= 0 ){
            throw new IOException("Error: wrong data");
        }
        else{
            this.side = side;
        }
    }

    @Override
    public double getArea(){
        return this.side*this.side;
    }

    public String printData(){
        return "Square data. side: " + this.side +" area: " + String.valueOf(getArea());
    }

    @Override
    public void increment(){
        this.side++;
    }
}
