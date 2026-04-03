class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # just like combo sum except have to prune solution if number already is in temp list
        res = []

        candidates.sort() # just nlogn so doesnt matter

        def dfs(i: int, curr: List[int], currSum: int):
            # base cases
            if currSum == target:
                res.append(curr.copy()) # make a copy since lists are mutable
                return
            # this needs to go second because what if the last element is part of a solution
            if i >= len(candidates): # index out of range bc no more nums to consider
                return

            # left decision tree - include number
            num = candidates[i]
            curr.append(num)
            dfs(i + 1, curr, currSum + num)

            # right decision tree - don't include number or ANY duplicates of number
            while i < len(candidates) and candidates[i] == num:
                i += 1
            curr.pop()
            dfs(i, curr, currSum)

        dfs(0, [], 0)
        return res