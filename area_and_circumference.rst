area and circumference
=======================

::

    #include <stdio.h>
    
    int main()
    {
        float r, a, c;
        printf("Enter radius: \n");
        scanf("%f", &r);
        a = 3.14*r*r;
        c = 2*3.14*r;
        printf("Area = %f\nCircumference = %f\n",a,c);
        return 0;
    }

