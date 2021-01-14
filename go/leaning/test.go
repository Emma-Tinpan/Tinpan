//Goの基本的な文法確認用コード

//行末までコメントアウト

/*
	複数の
	行に
	分けて
	コメントアウト
	できる
*/

/*
	fmtパッケージについて
	fmt.Println 文字列の錯誤に改行を添加した内容を標準出力する
	fmt.Printf　書式指定しを含んだフォーマット文字列と、それに続く可変長の引数を与え、生成した文字列を標準出力する
	print 引数として与えられた文字列を標準エラー出力する
*/

//文字列を改行付きで標準出力に出力する
fmt.Println("Hello, Golang") // => "Hello, Golang"
//任意の数の引数の場合、各文字列はスペースで区切られ、1行に連結する
fmt.Plrintln("My", "name", "is", "Taro") // => "My name is Taro"

//10進数、2進数、8進数、16進数を埋め込む
fmt.Printf("10進数=%d 2進数=%b 8進数=%o 16進数=%x\n", 10, 10, 10, 10)
// 書式指定子%vの使い方
fmt.Printf("数値=%v 文字列=%v 配列=%v\n", 5, "Golang", [...]int{1, 2, 3})
// 書式指定子%Tの使い方
fmt.Printf("数値=%T 文字列=%T 配列=%T\n", 5, "Golang", [...]int{1, 2, 3}) // => "数値=int 文字列=string 配列=[3]int"

