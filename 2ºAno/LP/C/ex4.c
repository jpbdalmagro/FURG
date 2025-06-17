#include <stdio.h>
#include <string.h>

void main() {
    int tempf;
    int tempc;

    printf("Digite a temperatura em Fahrenheit: ");
    scanf("%d", &tempf);
    tempc = (tempf - 32) * 5 / 9;
    printf("A temperatura em Celsius é: %d\n", tempc);
}