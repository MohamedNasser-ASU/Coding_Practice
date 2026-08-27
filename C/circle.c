// practice 2, circle 

#include <stdio.h>
#include <math.h>


int main(void){

    const float pi = acos(-1);
    double radius, area, volume, surfaceArea;

    printf("Enter the radius = ");
    scanf(" %lf", &radius);
    area = pi * radius*radius;
    surfaceArea = 4 * pi * pow(radius,2);
    volume = (4.0/3) * pi * pow(radius,3);

    printf("Circle area = %.2lf\n", area);
    printf("Sphere surface area = %.2lf\n", surfaceArea);
    printf("Sphere volume = %.2lf\n", volume);


    return 0;
}
