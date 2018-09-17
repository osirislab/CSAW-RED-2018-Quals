package main

import (
    "fmt"
    "os"
    "io/ioutil"
    "bufio"
)

func win(){
    fmt.Println("YOU WIN!!!!")
    flag, err := ioutil.ReadFile("flag.txt")
    if err != nil {
        fmt.Println(err)
        fmt.Println("You have solved the challenge but flag.txt does not exist try exploit remotely or contact one of us to get the matter resolved")
    }
    fmt.Println(string(flag))
}

func lose(){
    fmt.Println("YOU HAVE LOST!!!")
    os.Exit(0x1337)
}

func get_path() string {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    return string(text)
}

func traverse(path string, board [5][5]int, goal int ) bool {
    score := 0
    x := 0
    y := 0
    i := 0
    for x >= 0 && x <= 4 && y >= 0 && y <= 4 && i < len(path) - 1{
        step := string(path[i])
        //fmt.Println(step)
        if step == "R" {
            x += 1
        }else if step == "D"{
            y += 1
        }else if step == "L" {
            x -= 1
        } else if step == "U" {
            y -= 1
        } else {
            fmt.Println("Heyyy you can't go that way")
            os.Exit(0xbad)
        }
        score += board[x][y]
        i += 1;

//        fmt.Println(x,y)
    }
  //  fmt.Println(score)
    return score == goal
}

func main(){
    var board[5][5] int
    goal := 48

    for i := 0; i < 5; i++{
        for j := 0; j < 5; j++{
            board[i][j] = i + j
        }
    //    fmt.Println(board[i])
    }

    path := get_path()

    if traverse(path, board, goal){
        win()
    } else {
        lose()
    }
}
