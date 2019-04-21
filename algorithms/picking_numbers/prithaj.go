package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func intMax(a int32, b int32) int32{
    var maxInt int32
    if a > b{
        maxInt = a
    } else{
        maxInt = b
    }

    return maxInt
}

func pickingNumbers(a []int32) int32 {
    countMap := map[int32]int32 {}
    for _, val := range a{
        _, ok := countMap[val]
        if ok{
            countMap[val] +=1
        } else{
            countMap[val] = 1
        }
    }

    var biggestSubArrayLen int32 = 0
    for _, val := range a{
        var leftArrLen, rightArrLen int32 = 0, 0
        left, right := val-1, val+1
        _, leftok := countMap[left]
        _, rightok := countMap[right]

        if leftok{
            leftArrLen = countMap[val] + countMap[left]
        }

        if rightok{
            rightArrLen = countMap[val] + countMap[right]
        }

        var totalSubArrLen int32 = intMax(countMap[val], intMax(leftArrLen, rightArrLen))
        biggestSubArrayLen = intMax(biggestSubArrayLen, totalSubArrLen)
    }

    return biggestSubArrayLen

}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var a []int32

    for i := 0; i < int(n); i++ {
        aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
        checkError(err)
        aItem := int32(aItemTemp)
        a = append(a, aItem)
    }

    result := pickingNumbers(a)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}

