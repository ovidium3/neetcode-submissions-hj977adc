class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1 in range(len(numbers)):
            for i2 in range(len(numbers)):
                if numbers[i2] == target - numbers[i1] and i1 < i2:
                    return [i1 + 1, i2 + 1]