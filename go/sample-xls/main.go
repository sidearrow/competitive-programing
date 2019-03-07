package main

import (
	"fmt"
	"strconv"
	"github.com/extrame/xls"
)

func main() {
	workBook, _ := xls.Open("sample.xls", "utf-8")
	workSheet := workBook.GetSheet(0)
	fmt.Println("sheet name: " + workSheet.Name)
	for i := 0; i < 3; i++ {
		row := workSheet.Row(i)
		fmt.Println("first col: " + strconv.Itoa(row.FirstCol()))
		fmt.Println("first col: " + strconv.Itoa(row.LastCol()))
		fmt.Println("second col: " + row.Col(1))
	}
}
