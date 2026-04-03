class Solution: # O(n) time and space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = {}   #key = num, value = freq
        freqArray = [[] for i in range(len(nums) + 1)] # index = count, value = list of values, need +1 size in case where only 1 elt

        for num in nums:
            if num not in mostFreq:
                mostFreq[num] = 1
            else:
                mostFreq[num] += 1
            # can also be written as mostFreq[num] = 1 + mostFreq.get(num, 0) for one liner

        for key, val in mostFreq.items():
            freqArray[val].append(key) # index into frequency array, putting values with freq as index

        resList = []
        for i in range(len(freqArray) - 1, 0, -1): # loop backwards so start at k, down to 0, incr by -1
            for num in freqArray[i]:
                resList.append(num)
                if len(resList) == k:   # stop once you get k elts in list
                    return resList
