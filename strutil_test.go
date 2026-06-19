package strutil

import "testing"

func TestRepeat(t *testing.T) {
	if got := Repeat("ab", 3); got != "ababab" {
		t.Fatalf("Repeat(\"ab\", 3) = %q; want \"ababab\"", got)
	}
}
