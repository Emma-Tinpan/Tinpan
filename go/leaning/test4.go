package leaning

import {
	"fmt"
}

/* func [関数名] ([引数の定義]) [戻り値型]{
	[関数本体]
} */

func plus (x, y int) int {
	return x + y
}

//複数の戻り値を返す方法
func div(a, b int) (int, int) {
	q := a / b
	r := a % b
	return q,r
}

func main() {
	q, r := div (19, 7)
	fmt.Printf("商=%d 余剰=%d\n", q, r)
}

//定数の定義
const (
	x=1
	y=2
	z=3

)