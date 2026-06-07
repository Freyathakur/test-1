package calc

import "testing"

func TestAdd(t *testing.T) {
	cases := []struct {
		name       string
		a, b, want int
	}{
		{"two positives", 2, 3, 5},
		{"zero identity", 0, 7, 7},
	}
	for _, tc := range cases {
		if got := Add(tc.a, tc.b); got != tc.want {
			t.Errorf("%s: Add(%d,%d)=%d, want %d", tc.name, tc.a, tc.b, got, tc.want)
		}
	}
}
