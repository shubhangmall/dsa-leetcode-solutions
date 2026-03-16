class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            # base case — anything to the power of 0 is 1
            if n == 0:
                return 1.0
            # base case — 0 to any power is 0
            if x == 0:
                return 0.0
            
            # recursively compute x to the half power
            half = helper(x, n // 2)
            
            # if n is even — square the half result
            if n % 2 == 0:
                return half * half
            # if n is odd — square the half result and multiply by x once more
            else:
                return x * half * half
        
        # get result using absolute value of n
        result = helper(x, abs(n))
        
        # if n was negative return the reciprocal
        if n < 0:
            return 1 / result
        # if n was positive return result directly
        return result