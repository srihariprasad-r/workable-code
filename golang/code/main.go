package main

import (
	"fmt"
	"innerfunction/functionparms"
	"innerfunction/datastructs"
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
	//pass by value
	functionparms.SomeIncrement(score)
	fmt.Println("inside main passed by value: ", score)
	//pass by reference
	functionparms.PointerIncrement(&score)
	//slice
	fmt.Println("inside main passed by reference: ", score)
	slice.Slicefunction([]string {"Alice","Bob","Foo"})
}