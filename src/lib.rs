pub struct Point {
    pub x: i32,
    pub y: i32,
}

/// Render a point as text.
pub fn describe(p: Point) -> String {
    // bug: Point does not implement std::fmt::Display, so `{}` fails
    // to compile (E0277). Use `{:?}` with #[derive(Debug)] or impl
    // Display for Point.
    format!("{}", p)
}
