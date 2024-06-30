package slice

import "fmt"

func Slicefunction(user []string) {
	for idx, usr := range user {
		fmt.Println(usr , " occurs at index ", idx)
	}
}

func RemoveSlice(a []int, idx int) []int {
	return append(a[:idx], a[idx+1:]...)
}

func RemoveSlicePointer(b *[]int, idx int) []int {
	sliceOne := (*b)[:idx]  //pointer deference for arrays
	sliceTwo := (*b)[idx+1:]
	return append(sliceOne, sliceTwo...) 
}