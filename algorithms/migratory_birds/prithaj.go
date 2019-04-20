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
func migratoryBirds(arr []int32) int32 {
    countMap := map[int32]int32 {}
    var i int32
    for i = 0; i < int32(len(arr)); i++{
        _, birdIsPresent := countMap[arr[i]]
        if birdIsPresent{
            countMap[arr[i]] += 1
        } else{
            countMap[arr[i]] = 1
        }
    }

    var highestBirdFreq int32 = 0
    for _,freq := range countMap{
        highestBirdFreq = intMax(freq, highestBirdFreq)
    }
    
    var mostFrequentBird int32
    for bird,freq := range countMap{
        if freq == highestBirdFreq{
            mostFrequentBird = bird
            break
        }
    }

    return mostFrequentBird
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    arrCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(arrCount); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    result := migratoryBirds(arr)

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

