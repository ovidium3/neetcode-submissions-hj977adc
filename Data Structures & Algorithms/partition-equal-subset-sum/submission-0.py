class Solution: # O(n * sum(nums)) so technically O(n) time, O(sum(nums)) space since sum(nums) <= 50,000.
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 knapsack problem - put into one array or the other
        # first compute total sum, and add up ways to get to half of that.
        # odd sum cannot be partitioned by default, so that eliminates those automatically
        # maximum array sum is 50000 so will definitely fit in a 32bit integer
        # draw out 2^n decision tree to visualize possible sums
        # recurrence relation - work backwards so dp[n] = 
        # use a set to only hold unique values, and essentially check all possible sums to create from input array
        # size of the cache is O(sum(nums)) so 
        if sum(nums) % 2 == 1: # no way to partition a sum that is not even
            return False
        
        halfSum = sum(nums) / 2 # guaranteed to be a whole number
        dp = set([0]) # init with zero since that is a possible sum by selecting nothing
        
        for i in range(len(nums) - 1, -1, -1): # iterate backwards
            nextDP = dp.copy() # create copy for curr iteration, to add new elts based off old set
            for t in dp: # check each elt in old dp set
                if (t + nums[i]) == halfSum: # very good optimization to end search early
                    return True 
                nextDP.add(t + nums[i]) # add new summation with curr idx
            
            dp = nextDP # udpate final set to include new stuff
        
        return True if halfSum in dp else False