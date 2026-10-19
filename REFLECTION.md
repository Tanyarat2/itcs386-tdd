# Part B: Reflection

## 1. Tests, code lines, and ratio

Part A has 9 final tests and 39 lines of production code, excluding blank lines. The ratio is 9:39, about 1:4.33. There were 10 tests during development, but one was later removed.

## 2. Longest red interval

A7 had the most failing stages. The code returned 201 g instead of 228 g because it added amounts without converting units. The tests passed after both quantities were converted to grams before adding.

## 3. Three ways to get green

A1 used Fake It with the fixed value 600. A2 used Triangulate by adding another multiplication example. A8 used Obvious Implementation to multiply both sides of a sum. These choices kept each change small.

## 4. Remaining test-list items

All seven original items are complete, including A8. Hashability is still deferred because the lab does not need it. It should only be added when quantities need to be dictionary keys or set members.

## 5. Quantity.reduce and design

A possible first design would put all conversion code in `Converter`. The tests showed that giving both `Quantity` and `Sum` a `reduce` method makes conversion simpler.

## 6. Tests after code versus tests before code

In Part 0, tests checked existing code and found bugs. In Part A, tests guided the design. They led to returning new quantities, comparing values, creating sums, and converting units.