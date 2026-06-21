package calc

// Double returns twice n.
func Double(n int) int {
	// bug: `result` is never declared (should be `:=`)
	result = n * 2
	return result
}
