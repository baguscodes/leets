func addBinary(a string, b string) string {
    a = reverseString(a)
    b = reverseString(b)
    
    var result strings.Builder
    carry := 0
    maxLen := max(len(a), len(b))
    
    for i := 0; i < maxLen; i++ {
        bitA := 0
        bitB := 0
        
        if i < len(a) {
            bitA = int(a[i] - '0')
        }
        if i < len(b) {
            bitB = int(b[i] - '0')
        }
        
        total := bitA + bitB + carry
        carry = total / 2
        result.WriteByte(byte(total % 2 + '0'))
    }
    
    if carry > 0 {
        result.WriteByte('1')
    }

    return reverseString(result.String())
}

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}