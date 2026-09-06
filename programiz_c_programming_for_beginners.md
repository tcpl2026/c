# Programiz C Programming for Beginners

## c variables and print output

```
#include <stdio.h>

int main(){

    int age = 25;
    printf("Age: %d", age);

    age = 31;
    printf("\nNew age: %d", age);

    return 0;
}
```

```
#include <stdio.h>

int main() {

    int firstNumber = 33;
    printf("firstNumber = %d", firstNumber);

    int secondNumber = firstNumber;
    printf("\nsecondNumber = %d", secondNumber);

    return 0;
}

```

## data types in c programming

```
/*
int        (4 bytes) | %d for printing
double     (8 bytes) | %lf for printing
float      (4 bytes) | %f for printing
char       (1 bytes) | %c for printing
*/

#include <stdio.h>

int main() {
    int age = 10;
    printf("Age = %d\n", age);

    double number = 12.45;
    printf("%lf\n", number);
    printf("%.2lf\n", number);

    float number1 = 10.9f;
    printf("%f\n", number1);
    printf("%.1f\n", number1);

    double number2 = 5.5e6;
    printf("%lf\n", number2);

    char character = 'z';
    printf("%c\n", character);
    printf("%d\n", character);

    int age1;
    double number3;

    printf("int size = %zu", sizeof(age1));
    printf("\ndouble size = %zu", sizeof(number3));

    return 0;
}
```

## get user input

```
#include <stdio.h>

int main() {
    int age;

    printf("Enter input value: ");
    scanf("%d", &age);
    printf("Age = %d\n", age);

    double number;
    char alphabet;

    printf("Enter double input: ");
    scanf("%lf", &number);

    printf("Enter character input: ");
    scanf("\n%c", &alphabet);

    printf("Number: %lf", number);
    printf("\nCharacter: %c", alphabet);

    printf("Enter input values: ");
    scanf("%lf %c", &number, &alphabet);
    printf("Number: %lf\n", number);
    printf("Character: %c\n", alphabet);

    return 0;
}
```

## comments

```
#include <stdio.h>

int main() {
    // create a variable
    int data = 34;

    //print the value of data variable
    printf("Data = %d\n", data);

    int data1 = 34; // create a variable

    printf("Data = %d\n", data1); //print the value of data1 variable

    /* aa
     bb */

    return 0;
}
```

## c operators

```
// Additon             +
// Subtraction         -
// Multipliccation     *
// Division            /
// Remainder           %
// Increment           ++
// Decrement           --

#include <stdio.h>

int main() {
    int x = 12;

    int result = x + 8;

    printf("%d\n", result);
    printf("%d\n", x+8);


    double y = 12.57;

    double result1 = y + 8.67;

    printf("%.2lf\n", result1);


    int z = 12;

    printf("%d\n", z++);
    printf("%d\n", ++z);
    printf("%d\n", z--);
    printf("%d\n", --z);


    return 0;
}
```

## type conversion in c | implicit and explicit type conversion

```
#include <stdio.h>

int main()
{
    char a = '5';
    int b = 9;

    int result = a + b;

    printf("%d\n", result);

    /********************/

    double a1 = 5.67;
    int b1 = 9;

    int result1 = a1 + b1;

    printf("%d\n", result1);

    double result2 = a1 + b1;

    printf("%lf\n", result2);

    /********************/

    double a3 = 5.67;
    int b3 = 9;

    double result3 = (int)a3 + b3;

    printf("%lf\n", result3);

    /********************/

    int a4 = 9;
    int b4 = 2;

    double result4 = a4 / b4;
    double result44 = (double)a4 / b4;

    printf("%lf\n", result4);
    printf("%lf\n", result44);

    return 0;
}
```

## boolean and comparison operators

```
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool value1 = true;
    bool value2 = false;

    printf("%d\n", value1);
    printf("%d\n", value2);

    return 0;
}
```

```
/*
>    Greater than
<    Less than
==   Equal to
>=   Greater than or equal to
<=   Less than or equal to
!=   Not equal to
*/

#include <stdio.h>
#include <stdbool.h>

int main() {
    bool value = (12 > 9);

    printf("%d\n", value);

    return 0;
}
```

logical operators in c

```
/*
 * &&    AND
 * ||    OR
 * !     NOT
 */

#include <stdio.h>
#include <stdbool.h>

int main(){
    int age = 18;
    double height = 6.3;

    bool result = (age >= 18) && (height > 6.0);

    printf("%d\n", result);

    bool result1 = !(age >= 18);

    printf("%d\n", result1);

    return 0;
}
```

## if else statements in c

```
#include <stdio.h>

int main() {
    int  age = 15;

    if (age >= 18) {
        printf("You are eligible to vote\n");
    }
    else {
        printf("Sorry, you are not eligible to vote\n");
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {
    int  age = 15;

    if (age > 120) {
        printf("Invalid age");
    }
    else if (age < 0) {
        printf("Invalid age");
    }
    else if (age >= 18) {
        printf("You are eligible to vote\n");
    }
    else {
        printf("Sorry, you are not eligible to vote\n");
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {
    int  age = 15;

    if (age > 120 || age < 0) {
        printf("Invalid age");
    }
    else if (age >= 18) {
        printf("You are eligible to vote\n");
    }
    else {
        printf("Sorry, you are not eligible to vote\n");
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    int a = 5;

    if ( !(a % 2 == 0) ) {
        printf("Inside if\n");
    }
    else {
        printf("Inside else\n");
    }

    return 0;
}
```

## ternary operator in c

```
#include <stdio.h>

int main() {
    int age = 24;

    (age >= 18) ? printf("You can vote\n") : printf("You cannot vote\n");

    return 0;
}
```

```
#include <stdio.h>

int main() {
    char operator = '+';

    int num1 = 8;
    int num2 = 7;

    int result = (operator == '+') ? (num1 + num2) : (num1 - num2);
    printf("%d", result);

    return 0;
}
```

```
#include <stdio.h>

int main() {

    int result;

    if (5 > 3) {
        result = 5;
    }
    else {
        result = 3;
    }

    printf("%d\n", result);

    5 > 3 ? result = 5 : 3;

    printf("%d\n", result);

    return 0;
}
```

## switch statement

```
#include <stdio.h>

int main() {
    int number;
    printf("Enter the number between 1 to 7: ");
    scanf("%d", &number);

    switch(number) {
        case 1:
            printf("Sunday");
            break;
        case 2:
            printf("Monday");
            break;
        case 3:
            printf("Tuesday");
            break;
        case 4:
            printf("Wednesday");
            break;
        case 5:
            printf("Thursday");
            break;
        case 6:
            printf("Friday");
            break;
        case 7:
            printf("Saturday");
            break;
        default:
            printf("Invalid number");
    }
    putchar('\n');

    return 0;
}
```

不能漏掉break语句，如果移除break语句，匹配到的那一行后面的都会打印出来

```
#include <stdio.h>

int main() {
    int number;
    printf("Enter the number between 1 to 7: ");
    scanf("%d", &number);

    switch(number) {
        case 1:
            printf("Sunday");
        case 2:
            printf("Monday");
        case 3:
            printf("Tuesday");
        case 4:
            printf("Wednesday");
        case 5:
            printf("Thursday");
        case 6:
            printf("Friday");
        case 7:
            printf("Saturday");
        default:
            printf("Invalid number");
    }
    putchar('\n');

    return 0;
}
```

switch with multiple case

```
#include <stdio.h>

int main() {
    int number;
    printf("Enter the number between 1 to 7: ");
    scanf("%d", &number);

    switch(number) {
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            printf("Weekday");
            break;
        case 1:
        case 7:
            printf("Weekend");
            break;
        default:
            printf("Invalid number");
    }
    putchar('\n');

    return 0;
}
```

simple calculator

```
#include <stdio.h>

int main() {
    char operator;
    printf("Choose an operator ['+', '-', '*', '/']: ");
    scanf("%c", &operator);

    double num1, num2;

    printf("Enter first number: ");
    scanf("%lf", &num1);

    printf("Enter second number: ");
    scanf("%lf", &num2);

    double result;

    switch(operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
    }
    printf("%.2lf\n", result);

    return 0;
}
```

## while loop

```
#include <stdio.h>

int main() {
    int count = 1;

    while (count < 5) {
        printf("while loop in C\n");
        printf("Count = %d\n", count);
        count ++;
    }

    return 0;
}
```

create multiplication table

```
#include <stdio.h>

int main() {
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);

    int count = 1;
    while (count <= 10) {
        int product = number * count;
        printf("%d\n", product);
        count++;
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);

    int count = 1;
    while (count <= 10) {
        int product = number * count;
        printf("%d*%d = %d\n", number, count, product);
        count++;
    }

    return 0;
}
```

do...while loop

```
#include <stdio.h>

int main() {
    int count = 1;

    do {
        printf("%d\n", count);
        count++;
    } while (count < 5);

    return 0;
}
```

```
#include <stdio.h>

int main() {
    int count = 5;

    do {
        printf("%d\n", count);
        count++;
    } while (count < 5);

    return 0;
}
```

## for loop

```
#include <stdio.h>

int main() {

    for (int i = 1; i < 10; i++) {
        printf("%d ", i);
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    printf("%d\n", sum);

    return 0;
}
```

```
#include <stdio.h>

int main() {

    int sum = 0;
    for (int i = 2; i <= 100; i+=2) {
        sum += i;
    }
    printf("%d\n", sum);

    return 0;
}
```

## break and continue

```
#include <stdio.h>

int main() {

    for (int i = 1; i <= 5; i++) {
        printf("%d\n", i);
        break;
        printf("After the break");
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            break;
        }
        printf("%d\n", i);
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    while(1) {
        int number;
        printf("Enter a number: ");
        scanf("%d", &number);

        if (number < 0) {
            break;
        }
        printf("%d\n", number);
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue;
        }
        printf("%d\n", i);
    }

    return 0;
}
```

```
#include <stdio.h>

int main() {

    while(1) {
        int number;
        printf("Enter a number: ");
        scanf("%d", &number);

        if (number <= 0) {
            break;
        }

        if (number %2 != 0) {
            continue;
        }

        printf("%d\n", number);
    }

    return 0;
}
```

## c functions

```
returnType functionName {
    ...
    ...
}
```

```
#include <stdio.h>

void greet() {
    printf("Good morning\n");
}

int main() {

    greet();
    printf("After function call\n");

    return 0;
}
```

```
#include <stdio.h>

void calculateSquare(int number) {
    int square = number * number;
    printf("Square of %d is %d\n", number, square);
}

int main() {

    calculateSquare(5);

    return 0;
}
```

```
#include <stdio.h>

void addNumbers(int number1, int number2) {
    int sum = number1 + number2;
    printf("Sum of %d and %d is %d\n", number1, number2, sum);
}

int main() {

    addNumbers(8, 9);

    return 0;
}
```

```
#include <stdio.h>

int addNumbers(int number1, int number2) {
    int sum = number1 + number2;
    return sum;
}

int main() {

    int result = addNumbers(8, 9);
    printf("Result = %d\n", result);

    return 0;
}
```

function prototype

```
#include <stdio.h>

int addNumbers(int number1, int number2);

int main() {

    int result = addNumbers(8, 9);
    printf("Result = %d\n", result);

    return 0;
}

int addNumbers(int number1, int number2) {
    int sum = number1 + number2;
    return sum;
}
```

## c variable scope

local variable scope

```
#include <stdio.h>

void addNumbers(int number1, int number2) {
    int result = number1 + number2;
}

int main() {
    addNumbers(5, 6);
    printf("Result = %d", result);

    return 0;
}

error: ‘result’ undeclared (first use in this function)
```

global variable scope

```
#include <stdio.h>

int result;

void addNumbers(int number1, int number2) {
    result = number1 + number2;
}

int main() {
    addNumbers(5, 6);
    printf("Result = %d", result);

    return 0;
}
```

## c standard library functions

```
#include <stdio.h>
#include <math.h>

int main() {

    int num = 25;
    printf("Square root %lf\n", sqrt(num));

    return 0;
}

gcc 1.c -lm
```

```
#include <stdio.h>
#include <math.h>

int main() {

    int num = 27;
    printf("Cube root %lf\n", cbrt(num));

    return 0;
}
```

```
#include <stdio.h>
#include <math.h>

int main() {

    int a = 5, b = 2;

    double result = pow(a, b);
    printf("Power: %lf\n", result);

    return 0;
}
```

```
#include <stdio.h>
#include <ctype.h>

int main() {

    char alpha = 'e';
    char upper = toupper(alpha);

    printf("%c\n", upper);

    char lower = tolower(upper);
    printf("%c\n", lower);

    return 0;
}
```

## c recursion

```
#include <stdio.h>

int sum(int n);

int main() {
    int number, result;

    printf("Enter a positive integer: ");
    scanf("%d", &number);

    result = sum(number);

    printf("sum = %d\n", result);

    return 0;
}

int sum(int n) {
    if (n != 0) {
        // sum() function calls itself
        return n + sum(n-1);
    }
    else {
        return n;
    }
}
```

## c arrays


