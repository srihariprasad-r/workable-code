package variable

import "fmt"

var (
	level int
	name string
)

func Somef() {
	var roomBooked, passengers int = 15, 3
	fmt.Println(roomBooked, passengers)
	level = 10
	name = "Some name"
	fmt.Println(level, name)
}