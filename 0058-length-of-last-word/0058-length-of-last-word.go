func lengthOfLastWord(s string) int {
    subslice := strings.Fields(s)
    fmt.Println(subslice[len(subslice)-1])
    return len(subslice[len(subslice)-1])
}