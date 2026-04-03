class Solution: # O(n) time and O(1) mem since using two variables, NOT auxiliary array or stack space
    def climbStairs(self, n: int) -> int:
        # in dp, most important is to define the recurrence relation, as well as base cases
        # here, it is memo[i] = memo[i - 1] + memo[i - 2] (fibonacci sequence)
        # top down or bottom up approach - memoization is top down, tabulation is bottom up
        # recursion with DFS would be 2^n but youre repeating the same subproblem multiple times
        # you can save each solution and skip entire decision tree, roughly O(n) solving each subproblem once
        # dont even need entire extra O(n) array - instead just track ways for prev 2 steps
        #
        # base cases
        if n <= 3:
            return n
        # else have to calculate up to n
        twoBehind, oneBehind = 1, 1 # represents n = 1 and n = 2 respectively
        for i in range(3, n + 1): # start at 3 since for loop is 0-indexed, end at n + 1 since it is exclusive
            curr = twoBehind + oneBehind
            twoBehind = oneBehind
            oneBehind = curr
        return twoBehind + oneBehind # since we stop iterating at n, still have to add last two

        '''
        table = [ i for i in range(n + 1) ] # start off by putting in base cases, and overwrite later values
        for i in range(4, n + 1): # start at index 4, or 4th position since 0 and 1-3 are already correctly filled in
            table[i] = table[i - 1] + table[i - 2] # simply fibonacci sequence as recurrence relation
        
        return table[n] # since array is of size n + 1, so can index at n
        '''