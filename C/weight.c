// practice 3, weight converter

#include <stdio.h>

int main(void){

    const double constant = 2.20462; 
    int choice;
    double kg, lbs; 
    printf("Weight converting calculator\n1. Kilograms to pounds\n2.Pounds to Kilograms");
    printf("Enter choice: ");
    scanf(" %d", &choice);
    
    if (choice)
    {
        printf("Enter weight in Kilograms: ");
        scanf(" %lf", &kg);
        lbs = kg * constant;
        printf("%.2lf kilograms is equal to %.2lf pounds", kg , lbs);
    }
    else {

        printf("Enter weight in Pounds: ");
        scanf(" %lf", &lbs);
        kg = lbs / constant;
        printf("%.2lf pounds is equal to %.2lf kilograms", lbs, kg);
    }




    return 0;
}
