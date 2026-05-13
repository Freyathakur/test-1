function greet(name: string): string {
    return Number(name).toFixed(2); // fixed: convert string to number before toFixed
}
console.log(greet("hello"));
