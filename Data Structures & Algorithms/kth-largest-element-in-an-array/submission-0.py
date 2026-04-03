class Solution: # QuickSelect O(n) avg, O(n^2) worst case (just like quicksort)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        # heapify solution - O(k log(n))
        nums = [-n for n in nums] # turn nums all negative since we need a max heap
        heapq.heapify(nums) # turn nums into a max heap in O(n) time

        # cannot just index into a heapified array, must run heappop operation
        for i in range(k - 1): # heappop until we reach next elt as kth elt
            heapq.heappop(nums)
        
        return -heapq.heappop(nums) # have to turn num back to positive after popping

        # sorting solution - O(n log(n))
        nums.sort()
        return nums[len(nums) - k]
        '''

        # QuickSelect solution - runs poorly on leetcode but is supposedly the best solution
        k = len(nums) - k # turn k into k-th largest INDEX
        
        def quickSelect(l, r):
            pivot, p = nums[r], l # set pivot value as NUM at right idx, ptr to left IDX
            for i in range(l, r): # non inclusive of right index, no need to check past it
                if nums[i] <= pivot: # swap elts 
                    nums[p], nums[i] = nums[i], nums[p] # swap - one liner in py, not in c++ tho bc of parallel assignment and tuple unpacking
                    p += 1
            nums[p], nums[r] = nums[r], nums[p] # swap pivot num and rightmost num

            if p > k:
                return quickSelect(l, p - 1) # check left portion of array
            elif p < k:
                return quickSelect(p + 1, r) # check right portion of array
            else: # p == k so index is correct and ready to return
                return nums[p]

        return quickSelect(0, len(nums) - 1) # call func with proper range parameters