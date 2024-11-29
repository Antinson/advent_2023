package main

import (
    "bufio"
    "fmt"
    "os"
	"strings"
)

func main() {

	file, err := os.Open("1.txt")

	if err != nil {
        fmt.Println(err)
        return
    }

	defer file.Close()

	r := bufio.NewReader(file)

		for {
			line, err := r.ReadString('\n')
			if err != nil {
				break
			}

			fmt.Print(line)
		}
}

