pub fn add(a: i32, b: i32) -> i32 {
    // bug: trailing semicolon returns () instead of i32
    a + b;
}
