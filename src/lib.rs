pub fn factorial(n: u64) -> u64 {
    let mut acc = 1u64;
    // bug: exclusive range drops the final factor; should be 2..=n
    for i in 2..=n {
        acc *= i;
    }
    acc
}
