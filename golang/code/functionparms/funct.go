package functionparms

import (
	"fmt"
	"math"
)

var newscore int

type Rectangle struct {
	Width float64
	Height float64
}

func SomeIncrement(s int) {
	s += 10
	fmt.Println("inside functionparms package: ", s)
}

func PointerIncrement(s *int) {
	newscore = *s + 10
	*s = newscore
}

func Perimeter(r Rectangle) float64 {
	return 2*(r.Height * r.Width)
}

func (r Rectangle) PerimeterValueReference() float64 {
	r.Height = 20.0		//updates only copy
	return 2*(r.Height * r.Width)
}

func (r *Rectangle) PerimeterPointerReference() float64 {
	r.Height = 20.0		//updates actual memory location
	return 2*(r.Height * r.Width)
}

func ListRectanglesPointerReference(rc []*Rectangle) []float64 {
	var res = make([]float64, 2, 2)
	for _, rct := range rc {
		rct.Height = math.Sqrt(2) * rct.Height
		res = append(res, 2*(rct.Height + rct.Width))
	}

	return res
}