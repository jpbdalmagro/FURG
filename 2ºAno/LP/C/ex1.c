#include <stdio.h>
#include <string.h> 

int main(){
    int num;
    int fat = 1;
    printf("Digite um número: ");
    scanf("%d", &num);

    for (int i = 1; i <= num; i++){
        fat *= i;
    }
    printf("O fatorial de %d é %d\n", num, fat);
    return 0;
}