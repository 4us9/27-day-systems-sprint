# Merge Sort

**Time Complexity**: n(log(n))
- The constant inside log is not relevant to Big O notation. 
- Splitting trees is of log(n) time
- The merging is what is (n) times. 
- So it is work per level times the depth. Giving n(log(n)).

*Big O is <=.*
*So f is the slower (or equal) function on the left, 
g is the faster (or equal) function on the right. Your job is to sort them from "slowest to grow" to "fastest to grow" using Big-O as your comparison operator.*

**k-way Merge Sort (Successive Merging)**
- Sum of integers from 1 to k is (k(k+1))/2 giving k^2
- And given the arrays you just multiply.
- Theta(nk^2)

*You are touching these elements over and over again.*
