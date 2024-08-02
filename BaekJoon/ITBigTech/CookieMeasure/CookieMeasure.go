package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	userInput, _ := reader.ReadString('\n')
	userInput = strings.TrimSpace(userInput)
	N, _ := strconv.Atoi(userInput)

	// head := make([]int, 2)
	// 이렇게 하면 [0 0]이 기본으로 돼서 추가하면 [0 0 3 3] 이래 됨

	var head []int

	for i := 0; i < N; i++ {
		userInput, _ := reader.ReadString('\n')
		userInput = strings.TrimSpace(userInput)
		if strings.Contains(userInput, "*") {
			head = append(head, i+2)
			head = append(head, strings.Index(userInput, "*")+1)
			break
		}
	}

}
