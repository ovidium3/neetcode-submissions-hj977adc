# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        numPairs = len(pairs)
        result = [] #intermediate stages list

        for rPtr in range(numPairs):
            lPtr = rPtr - 1
            
            while lPtr >= 0 and pairs[lPtr].key > pairs[lPtr + 1].key:
                pairs[lPtr], pairs[lPtr + 1] = pairs[lPtr + 1], pairs[lPtr]
                lPtr -= 1

            result.append(pairs[:]) # clone since we still work with obj

        return result