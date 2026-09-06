# linlili

## 6

```
int main() {
    return 0;
}
```

#include <stdio.h>

int main() {
    printf("a\n");
    return 0;
}

#include <stdio.h>

int main() {
    printf("She said \"OK!\"\n");
    printf("\\");
    printf("\n");
    return 0;
}

#include <stdio.h>

int main() {
    printf("城市\t景点\n");
    printf("武汉市\t长江大桥\n");
    printf("天津市\t盘山\n");
    printf("泰安市\t岱庙\n");
    return 0;
}

------------------------

#include <stdio.h>

int main() {
    printf("Hello\bWorld");
    return 0;
}

-----------------------

#include <stdio.h>

int main() {
    printf("Hello\rWorld");
    return 0;
}

#include <stdio.h>

int main() {
    printf("   *\n");
    printf("  ***\n");
    printf(" *****\n");
    printf("*******\n");
    printf("==================\n");
    printf("This is a \"double quoted\" text. And here is a backslash\\.\n");
    return 0;
}

#include <stdio.h>

int main() {
    /* comment
     comment
     comment
     */
    int age = 10; //comment
    printf("Age: %d\n", age); //comment
}

#include <stdio.h>

int main() {
    printf("500的八进制为%o\n", 500);
    printf("500的十六进制为%x\n", 500);
    printf("500的十六进制为%X\n", 500);

    printf("500的八进制为%#o\n", 500);
    printf("500的十六进制为%#x\n", 500);
    printf("500的十六进制为%#X\n", 500);


    printf("八进制数764的十进制为%d\n", 0764);
    printf("十六进制数1f4的十进制为%d\n", 0x1f4);

    return 0;
}

