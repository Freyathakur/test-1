export function double(n: number): number {
  return n * 2;
}

// bug: passing a string to a number parameter
export const result: number = double(Number("5"));
