class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force using DFS - O(2^n) which is horrible - modify to get to n^2
        # draw out a decision tree to visualize but it will be a leftward stick after pruning
        # can do a DFS with caching by tracking the remaining result from a given index
        # true DP approach starts from the end and works backwards by computing earlier sequence len using later sequence len
        # recurrence relation - LIS[n] = max(LIS[n - 1], ...) if the prev elt is smaller else 1

        LIS = [1] * (len(nums)) # default length is just 1 element
        #LIS[len(nums)] = 1 # base case that is already initialized. this just for show.

        for i in range(len(nums) - 1, -1, -1): # fill table in reverse order
            for j in range(i + 1, len(nums)): # inclusive, exclusive so need +1
                if nums[j] > nums[i]: # compare to current number to determine if you consider for max
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # add one to length if the curr num is larger
            
        return max(LIS)