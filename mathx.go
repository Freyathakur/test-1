package mathx

func Double(n int) int {
	return n * 2
}

func Quad(n int) int {
	// bug: typo — should call Double, not double
	return Double(n) * 2
}
