use svc::factorial;

#[test]
fn test_factorial() {
    assert_eq!(factorial(4), 24);
}
