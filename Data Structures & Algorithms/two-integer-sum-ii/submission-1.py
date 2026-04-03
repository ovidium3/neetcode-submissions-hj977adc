class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force solution
        # for i1 in range(len(numbers)):
        #     for i2 in range(len(numbers)):
        #         if numbers[i2] == target - numbers[i1] and i1 < i2:
        #             return [i1 + 1, i2 + 1]

        # actual solution 2 ptrs
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1