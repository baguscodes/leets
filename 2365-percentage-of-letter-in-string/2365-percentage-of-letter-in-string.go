func percentageLetter(s string, letter byte) int {
    str := strings.Split(s,"")
    strLen := float64(len(str))
    
    //get letter count
    var letterCount float64
    for l,_ := range str{
        if str[l]==string(letter){
            letterCount++
            fmt.Println("Letter found")
        }
    }

    fmt.Println("Letter found : ", letterCount)
    fmt.Println("strLen : ", strLen)
    //count percentage
    result := int(math.Floor((letterCount/strLen) * 100))
    fmt.Println(str)
    fmt.Println(result)
    return result
}