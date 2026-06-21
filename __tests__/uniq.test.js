const { uniq } = require("../index");

test("uniq dedups", () => {
  expect(uniq([1, 1, 2, 3, 3])).toEqual([1, 2, 3]);
});
