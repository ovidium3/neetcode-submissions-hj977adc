class Solution: # O(2 ^ target)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute force - decision tree with a branch for each number. doesnt work bc this gives perms not combos
        # instead, decision tree where one side keeps adding same number, other side moves on to the next number.
        # use an i ptr to keep track of which number we are on
        res = [] # global result var

        def dfs(i: int, curr: List[int], currSum: int) -> None:
            # base cases
            if currSum == target: # successful combo
                res.append(curr.copy())
                return
            if i >= len(nums) or currSum > target: # unsuccessful combo
                return

            toAdd = nums[i]
            curr.append(toAdd)

            dfs(i, curr, currSum + toAdd) # left decision: proceed with same number

            curr.pop()
            dfs(i + 1, curr, currSum) # right decision: proceed with next number

        dfs(0, [], 0)
        return res