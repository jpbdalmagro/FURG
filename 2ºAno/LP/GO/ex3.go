package main

import(
	"fmt"
)

func main(){
	var(
		num int
		cont = 0
	)

	fmt.Print("Digite o quantos números ímpares quer ver: ")
	fmt.Scan(&num)
	fmt.Printf("Os primeiros %d números impares são: ")

	for i := 1; cont < num; i++{
		if i % 2 == 1{
			fmt.Printf("%d, ", i)
			cont += 1
		}
	} 
}