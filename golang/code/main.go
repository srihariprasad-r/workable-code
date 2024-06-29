package main

import (
	"fmt"
	"innerfunction/functionparms"
	"innerfunction/variable"
	"time"
)

var score int

func main() {
	now := time.Now()
	fmt.Println(now)
	variable.Somef()	
	//Newfunc()		// go run .\main.go <depedent file>
	score = 10
	functionparms.SomeIncrement(score)
	fmt.Println("inside main passed by value: ", score)
	//pass by reference
	functionparms.PointerIncrement(&score)
	fmt.Println("inside main passed by reference: ", score)
}