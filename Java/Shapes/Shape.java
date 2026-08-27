package Shapes;

public class Shape implements Comparable<Shape>,Runnable {

    public Shape() {
    }

    public double getArea() {
        return 0;
    }

    @Override
    public int compareTo(Shape o)
    {
        if (this.getArea() > o.getArea())
        { return 1; }
        else if (this.getArea() < o.getArea())
        { return -1; }
        else return 0;
    }


    public boolean equals (Shape o){
        if (this.getArea() == o.getArea())
            return true;
        else return false;
    }


    public void increment(){}

    public String printData(){
        return null;
    }

    @Override
    public void run() {
        increment();
    }
}

