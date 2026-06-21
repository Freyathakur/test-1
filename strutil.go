package strutil

import "strings"

// Repeat returns s concatenated n times.
func Repeat(s string, n int) string {
	return strings.Repeat(s, n)
}
