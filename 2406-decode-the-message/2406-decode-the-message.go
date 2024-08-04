func decodeMessage(key string, message string) string {
    // Strip spaces and recurring letters
    keys := strings.ReplaceAll(key, " ", "")
    keys = removeRecurringLetters(keys)
    fmt.Println("KEYS:", keys)
    
    // Create decoder map: key=keys, value=alphabet
    decoder := make(map[rune]rune)
    alphabet := "abcdefghijklmnopqrstuvwxyz"

    for i, char := range keys {
        decoder[char] = rune(alphabet[i])
    }
    fmt.Println("DECODER:", decoder)
    
    // Decode the message
    var decoded []rune
    for _, char := range message {
        if decodedChar, found := decoder[char]; found {
            decoded = append(decoded, decodedChar)
        } else {
            decoded = append(decoded, char) // Keep the character as it is if not in the decoder
        }
    }

    return string(decoded)
}

func removeRecurringLetters(str string) string {
    seen := make(map[rune]bool)
    result := []rune{}

    for _, char := range str {
        if !seen[char] {
            seen[char] = true
            result = append(result, char)
        }
    }

    return string(result)
}