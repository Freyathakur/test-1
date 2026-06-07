// Package strutil provides simple string utilities.
package strutil

import "strings"

// Reverse returns the string with its characters in reverse order.
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i > j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// IsPalindrome reports whether s reads the same forwards and backwards
// (case-insensitive, ignoring spaces).
func IsPalindrome(s string) bool {
	cleaned := strings.ToLower(strings.ReplaceAll(s, " ", ""))
	reversed := Reverse(cleaned)
	return cleaned == reversed
}

// WordCount returns the number of whitespace-delimited words in s.
func WordCount(s string) int {
	fields := strings.Fields(s)
	return len(fields)
}

// Clamp returns value clamped to [lo, hi].
func Clamp(value, lo, hi int) int {
	if value < lo {
		return lo
	}
	if value > hi {
		return hi
	}
	return value
}
