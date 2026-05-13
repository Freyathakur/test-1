function greet(name: string): string {
    return name.toUpperCase().toFixed(2); // bug: string has no toFixed
}
console.log(greet("hello"));
