#include <stdio.h>
#include <string.h>

void main(){
    int num;

    printf("Digite um número: ");
    scanf("%d", &num);

    printf("Os primeiros %d números ímpares são: ", num);
    for (int i = 1; num > 0; i++){
        if (i % 2 == 1){
            printf("%d ", i);
            num--;
        }
    }
    printf("\n");
}