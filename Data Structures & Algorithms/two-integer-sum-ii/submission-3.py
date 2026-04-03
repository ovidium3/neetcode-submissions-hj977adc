class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # optimal solution: 2 ptrs since sorted and we
        # GUARANTEE a solution, always 1 valid sol
        l, r = 0, len(numbers) - 1
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return [l + 1, r + 1]
            elif sums < target:
                l += 1
            else:
                r -= 1

        
        
        # brute force: n^2 iteration constant space
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]