package main

import (
	"fmt"
	"innerfunction/datastructs"
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
	//pass by value
	functionparms.SomeIncrement(score)
	fmt.Println("inside main passed by value: ", score)
	//pass by reference
	functionparms.PointerIncrement(&score)
	//slice
	fmt.Println("inside main passed by reference: ", score)
	slice.Slicefunction([]string {"Alice","Bob","Foo"})

	var nums []int
	nums = append(nums, 1,2,3,4,5,6)
	copiedArr := make([]int, len(nums), cap(nums))
	copy(copiedArr, nums)

	fmt.Println("before remove at index: " , nums)
	//slice copies  & alters original array, so recapture with same variable to change both
	newarr := slice.RemoveSlice(nums, 2)
	fmt.Println("after remove at index in original array: " , nums)
	fmt.Println("after remove at index in sliced array: " , newarr)
	//use pointer
	fmt.Println("copied array: " , copiedArr)
	newarr1 := slice.RemoveSlicePointer(&copiedArr, 2)
	fmt.Println("after remove at index in original array: " , copiedArr)
	fmt.Println("after remove at index in sliced array: " , newarr1)	

	slice.Sliceproperty()
	
	// narr := []int{2, 4, 1, 3, 7}
	// n := slice.SortArrays(narr)
	// fmt.Println("sorted array: ", n)

	slice.SortArraysByComparator()
}