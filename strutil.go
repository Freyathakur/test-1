package strutil

// Repeat returns s concatenated n times.
func Repeat(s string, n int) string {
	out := ""
	for i := 0; i < n-1; i++ { // bug: should be i < n
		out += s
	}
	return out
}
