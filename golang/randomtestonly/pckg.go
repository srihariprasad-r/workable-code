package main

//import "fmt"

type Inter interface{ assume(s int) (*X, error) }

type X struct{ xs int}

func NewX(s int) *X {
	return &X{xs: s}
}

func (x *X) assume(h int) (*X, error) {
	return &X{x.xs + h}, nil
}

// func main() {
// 	k, _ := newX(2)
// 	fmt.Println(k.assume(3))
// 	fmt.Println("value of k: ", k)
// 	fmt.Println("address of k: " , &k)
// 	k, _ = newX(1)
// 	k.assume(7)		
// 	fmt.Println("value of k: ", k)
// 	fmt.Println("address of k: " , &k)
// }