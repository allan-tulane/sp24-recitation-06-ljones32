# CMPS 2200 Recitation 06
## Answers

**Name:** London Jones


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
T(n) = T(n-1) + T(n-2) + O(1), for n ≥ 2
T(0) = T(1) = O(1)

T(n) = O(2^n)

- **3)** 
S(n) = S(n-1) + O(1), for n ≥ 2
S(0) = S(1) = O(1)


S(n) = O(n)

- **4)**

Every num is the result of the previous two added together. 

- **6)**
T(n) = T(n-1) + T(n-2) + O(1), T(0) = T(1) = O(1)
So once.

Work: O(n)
Span: O(n)

- **8)**

When computing Fn using fib_bottom_up, each Fi will be read at most twice for any value i.

The work of fib_bottom_up is O(n), and the span is O(n)**