class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r): # m ptr optional here
            lCopy, rCopy = arr[l:m+1], arr[m+1:r+1] # non inclusive m+1
            i, j, k = l, 0, 0

            while j < len(lCopy) and k < len(rCopy):
                if lCopy[j] <= rCopy[k]:
                    arr[i] = lCopy[j]
                    j += 1
                else: # lCopy[j] > rCopy[k]
                    arr[i] = rCopy[k]
                    k += 1
                i += 1
            # only one executes. dont knwo which so put both
            while j < len(lCopy):
                nums[i] = lCopy[j]
                j += 1
                i += 1
            while k < len(rCopy):
                nums[i] = rCopy[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r) # do not reprocess left, so +1

            merge(arr, l, m, r)
            return arr

        l, r = 0, len(nums) - 1
        return mergeSort(nums, l, r)
        #return nums

        # valid solution, O(n) extra space tho
        # minHeap = []
        # for n in nums:
        #     heapq.heappush(minHeap, n)
        
        # res = []
        # for i in range(len(minHeap)):
        #     res.append(heapq.heappop(minHeap))
        # return res