package main

import (
	"fmt"
)

func main() {
	cfg := &Some{Interf: NewX(1)}
	s, _ := NewServer(cfg)
	fmt.Println(&s)
}
