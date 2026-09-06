for loop
========

Example: Basic for Loop

::

    #include <stdio.h>
    
    int main(){
       int a;
    
       for(a = 1; a <= 5; a++){
          printf("a: %d\n", a);
       }
    
       return 0;
    }

Initializing for Loop Counter Before Loop Statement

::

    #include <stdio.h>
    
        int main(){
           int a = 1;
        
           // for loop execution
           for( ; a <= 5; a++){
              printf("a: %d\n", a);
           }
           return 0;
        }

Updating Loop Counter Inside for Loop Body

::

    #include <stdio.h>
    
    int main(){
    
       int a;
    
       // for loop execution
       for(a = 1; a <= 5; ){
          printf("a: %d\n", a);
          a++;
       }
       return 0;
    }

Using Test Condition Inside for Loop Body

::

    #include <stdio.h>
    
        int main(){
           int a;
        
           // for loop execution
           for(a = 1; ; a++){
              printf("a: %d\n", a);
              if(a == 5)
              break;
           }
           return 0;
        }

Using for Loops with Multiple Counters

::

    #include <stdio.h>
    
        int main(){
           int a, b;
        
           // for loop execution
           for(a = 1, b = 1; a <= 5; a++, b++){
              printf("a: %d b: %d a*b: %d\n", a, b, a*b);
           }
        
           return 0;
        }

Decrement in for Loop

::

    #include <stdio.h>
    int main(){
       int a;
    
       // for loop execution
       for(a = 5; a >= 1; a--){
          printf("a: %d\n", a);
       }
    
       return 0;
    }

Traversing Arrays with for Loops

::

    #include <stdio.h>
    
    int main(){
       int i;
       int arr[] = {10, 20, 30, 40, 50};
    
       // for loop execution
       for(i = 0; i < 5; i++){
          printf("a[%d]: %d\n", i, arr[i]);
       }
    
       return 0;
    }

Example: Sum of Array Elements Using for Loop

::

    #include <stdio.h>
    int main(){
       int i;
       int arr[] = {10, 20, 30, 40, 50};
       int sum = 0;
       float avg;
    
       // for loop execution
       for(i=0; i<5; i++){
          sum += arr[i];
       }
       avg = (float)sum / 5;
       printf ("Average = %f", avg);
    
       return 0;
    }

Example: Factorial Using for Loop

::

    #include <stdio.h>
    
    int main(){
    
       int i, x = 5;
       int fact = 1;
    
       // for loop execution
       for(i=1; i<= x; i++){
          fact *= i;
       }
       printf("%d != %d", x, fact);
    
       return 0;
    }

