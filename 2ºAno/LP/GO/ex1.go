package main

import "fmt"

func main(){
	var base, expoente int
	fmt.Print("Digite o número a ser multiplicado: ")
	fmt.Scan(&base)
	fmt.Print("Digite o expoente: ")
	fmt.Scan(&expoente)

	resultado := base
	for i := 1; i < expoente; i++{
		resultado *= base
	}

	fmt.Println("O resultado da operação é", resultado)
}