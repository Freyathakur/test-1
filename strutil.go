package strutil

// Repeat returns s concatenated n times.
func Repeat(s string, n int) string {
	out := ""
	for i := 0; i < n; i++ {
		out += s
	}
	return out
}
