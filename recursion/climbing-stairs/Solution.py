# F(n) = F(n - 1) + F(n - 2)
# F(0) = 0, F(1) = 1
# Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones 
# In this problem, we use the Fibonacci sequence except the only difference is that it uses a different base case

"""
this solution accounts for the number of ways you could climb stairs given two different
possibilties combined together where both conditions are if you take 1 step or if you take 2 steps.
climbStairs(n)

"What can I do from here?"

        ↓

    Take 1 step
        ↓

solve the smaller problem n - 1

        +

    Take 2 steps
        ↓

solve the smaller problem n - 2

--------------------------------

what returns is 

↓

number of ways if I take 1 step first

+

number of ways if I take 2 steps first

--------------------------------

      what this could look like

             ↓

        climbStairs(2)
        /              \
       1                2
       ↓                ↓
climbStairs(1)    climbStairs(0)
      ↓                 ↓
     (1)                (1)

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        # base cases which is different from the conventional Fibonacci sequences base case
        if n == 0 or n == 1:
            return 1

        # recursive case
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
