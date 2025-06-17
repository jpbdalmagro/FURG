package main

import(
	"fmt"
)

func main(){
	var(
		tempF float32
		tempC float32
	)

	fmt.Print("Digite uma temperatura em Fahrentheit: ")
	fmt.Scan(&tempF)

	tempC = (tempF - 32) * 5 / 9

	fmt.Printf("%.1f°F equivalem a %.1f°C.\n", tempF, tempC)
}

