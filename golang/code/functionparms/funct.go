package functionparms

import "fmt"

var newscore int

func SomeIncrement(s int) {
	s += 10
	fmt.Println("inside functionparms package: ", s)
}

func PointerIncrement(s *int) {
	newscore = *s + 10
	*s = newscore
}