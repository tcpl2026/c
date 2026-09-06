while loop
===========

Example of while Loop in C

::

    #include <stdio.h>
    
    int main(){
    
       int a = 1;
    
       while(a <= 5){
          printf("Hello \n");
          a++;
       }
       printf("End of loop");
       return 0;
    }

Using while as Conditional Loop

::

    #include <stdio.h>
    
    int main(){
    
       int x = 0;
    
       while(x >= 0){
          (x % 2 == 0) ? printf("%d is Even \n", x) : printf("%d is Odd \n", x);
    
          printf("\n Enter a positive number: ");
          scanf("%d", &x);
       }
       printf("\n End of loop");
       return 0;
    }

Printing Lowercase Alphabets

::

    #include <stdio.h>
    
    int main(){
    
       char a = 'a';
    
       while(a <= 'z') {
          printf("%c", a);
          a++;
       }
       printf("\n End of loop");
       return 0;
    }

Equate Two Variables

::

    #include <stdio.h>
    
    int main(){
    
       int a = 10, b = 0;
    
       while(a != b){
          a--;
          b++;
          printf("a: %d b: %d\n", a,b);
       }
       printf("\n End of loop");
       return 0;
    }

