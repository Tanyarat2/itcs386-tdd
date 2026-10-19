# Part B: Reflection (draft for student review)

This draft describes the recorded AI-assisted workflow. It should be
reviewed and personalized before submission; no claim is made about
the student's unreported feelings or difficulties. Observations can be
checked against the Git history and evidence directory.

## 1. Tests, production lines, and ratio

The final Part A suite has 9 test functions, and `kitchen.py` has
39 nonblank, noncomment production lines (57 physical lines
including blank lines). The ratio of test functions to nonblank
production lines is 9:39, or approximately 1:4.33.
A2's temporary multiplication-by-two test was also written and later
removed at A3, so 10 distinct Part A test functions were written
over the exercise, while 9 remain in the final suite.

## 2. Longest red interval

A7 required the most consecutive red stages: the mixed-unit test first
exposed the missing `add_rate`, then the incorrect raw sum of 201 g,
and remained red while rates were stored and the converter was passed
through reduction. Green returned when each side was converted before
addition. This is the longest sequence of implementation-stage red
runs; individual pytest durations in the evidence files measure test
execution, not the student's thinking time. The student should add
their own experience if a personal elapsed-time answer is required.

## 3. Fake It, Triangulate, and Obvious Implementation

A1 used Fake It by assigning 600, proving that the first test was wired
to the implementation. A2 triangulated with multiplication by two,
whose expected 400 forced the hard-coded constant to become a formula.
A8 used Obvious Implementation: `Sum.times` multiplies both operands
and returns a new sum. These choices matched the prescribed learning
goals: small steps established confidence early, and the existing
expression structure made A8 a short, direct implementation.

## 4. Remaining test-list items

All seven original behaviors, including optional A8, are checked off.
Hashability remains explicitly deferred because A4 asked that the
concern be recorded without implementing it. There is no required
feature left to implement next; hashability should wait for an actual
caller needing dictionary keys or set membership. Other hypothetical
features were not added to the list, so there is no additional
speculative feature to delete.

## 5. Quantity.reduce and design

`Quantity.reduce` now returns a quantity in the target unit using a
converter's directional rate. A paper-first design might have put all
conversion logic in `Converter` and treated individual quantities and
sums separately. The tests instead led both expression types to expose
the same reduction operation, allowing the converter to delegate.
Whether I personally would have anticipated this method needs my own
review before submitting this draft.

## 6. Tests after code versus tests before code

Part 0 tested an existing implementation, checking its stated behavior
and exposing the three shipping defects at boundaries and rounding.
Part A used failing tests to change the API: A3 required returned values
instead of mutation, A4 motivated equality, A6 introduced deferred sums,
and A7 introduced conversion during reduction. That is an observable
difference in how tests shaped the design. The student should add how
the two approaches personally felt after reviewing and running them.
