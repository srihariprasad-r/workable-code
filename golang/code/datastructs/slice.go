package slice

import "fmt"

func Slicefunction(user []string) {
	for idx, usr := range user {
		fmt.Println(usr , " occurs at index ", idx)
	}
}