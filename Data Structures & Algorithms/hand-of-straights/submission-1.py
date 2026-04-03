class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        nums = Counter(hand)

        for num in hand:
            start = num
            while nums[start - 1]:
                start -= 1
            # decrement start until we know that we
            # can start at smallest val
            # since there MUST be a sol, can check
            # to see starting at smallest val in nums
            while start <= num:
                while nums[start]:
                    for i in range(start, start + groupSize):
                        if not nums[i]:
                            return False
                        nums[i] -= 1
                start += 1
        return True