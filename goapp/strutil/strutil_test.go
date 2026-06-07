package strutil_test

import (
	"testing"

	"github.com/Freyathakur/test-1/goapp/strutil"
)

func TestReverse(t *testing.T) {
	cases := []struct {
		input string
		want  string
	}{
		{"hello", "olleh"},
		{"", ""},
		{"a", "a"},
		{"abcd", "dcba"},
	}
	for _, tc := range cases {
		got := strutil.Reverse(tc.input)
		if got != tc.want {
			t.Errorf("Reverse(%q) = %q; want %q", tc.input, got, tc.want)
		}
	}
}

func TestIsPalindrome(t *testing.T) {
	cases := []struct {
		input string
		want  bool
	}{
		{"racecar", true},
		{"A man a plan a canal Panama", true},
		{"hello", false},
		{"", true},
	}
	for _, tc := range cases {
		got := strutil.IsPalindrome(tc.input)
		if got != tc.want {
			t.Errorf("IsPalindrome(%q) = %v; want %v", tc.input, got, tc.want)
		}
	}
}

func TestWordCount(t *testing.T) {
	cases := []struct {
		input string
		want  int
	}{
		{"hello world", 2},
		{"", 0},
		{"  ", 0},
		{"one", 1},
		{"a b c d", 4},
	}
	for _, tc := range cases {
		got := strutil.WordCount(tc.input)
		if got != tc.want {
			t.Errorf("WordCount(%q) = %d; want %d", tc.input, got, tc.want)
		}
	}
}

func TestClamp(t *testing.T) {
	cases := []struct {
		value, lo, hi int
		want          int
	}{
		{5, 0, 10, 5},
		{-3, 0, 10, 0},
		{15, 0, 10, 10},
		{0, 0, 0, 0},
	}
	for _, tc := range cases {
		got := strutil.Clamp(tc.value, tc.lo, tc.hi)
		if got != tc.want {
			t.Errorf("Clamp(%d, %d, %d) = %d; want %d", tc.value, tc.lo, tc.hi, got, tc.want)
		}
	}
}
