package main

import(
	"fmt"
)

func main(){
	var(
		num int
		prime = true	
	)

	fmt.Print("Digite um número: ")
	fmt.Scan(&num)

	if num < 2{
		prime = false
	} else {
		for i := 1; i <= num / 2; i++{
			if num % i == 2{
				prime = false
				break
			}
		}
	}

	if prime {
		fmt.Printf("O número %d é primo\n", num)
	} else {
		fmt.Printf("O número %d não é primo\n", num)
	}
}
