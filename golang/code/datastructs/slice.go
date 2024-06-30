package slice

import (
	"fmt"
	"sort"
)

type mySort []int

func (s mySort) Len() int {
	return len(s)
}

func (s mySort) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s mySort) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]		
}


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

func Sliceproperty() {
	var nums []int
	nums = append(nums, 1, 2, 3, 4, 5, 6)
	nums1 := nums[0:3] //slice does not copy , but points to original array
	//update slice
	nums1[0] = 99
	fmt.Println(nums)
	fmt.Println(nums1)	
	//update original array
	nums[2] = 77
	fmt.Println(nums) 
	fmt.Println(nums1)		
	
	fmt.Print("slice print in foor loop:")
	for _, n := range nums1 {
		fmt.Printf(" %d " , n)
	}
	fmt.Println()
}

func SortArraysByComparator() {
	//sort.Ints(o)
	//return o
	var nums mySort = []int{2,3,4,1,0,5}
	sort.Sort(nums)
	fmt.Println(nums)
	
}