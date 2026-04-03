class Solution: # O(n) time comp
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # go from right to left since two cars could collide and slow down
        # delete from left since theyre gonna catch up and no car will pass both anyway so only need 1
        pair = [[p, s] for p, s in zip(position, speed)] # list comp in python. can also use hashmaps

        stack = []

        for p, s in sorted(pair)[::-1]: # reverse sorted order
            remainingTime = (target - p) / s # decimal division as opposed to int division (//)
            stack.append(remainingTime)
            # need at least 2 cars bc if theres only 1 car, dont need to do anything
            # check if car at top of stack reaches dest before one ahead, pop from stack top
            # if statement instead of while since we check reverse order so impossible to collide with ahead
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)