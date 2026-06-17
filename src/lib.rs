pub fn factorial(n: u64) -> u64 {
    let mut acc = 1u64;
    // fix: use inclusive range to multiply all numbers from 2 to n
    for i in 2..=n {
        acc *= i;
    }
    acc
}
