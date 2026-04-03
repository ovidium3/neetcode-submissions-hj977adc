class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                topVal = stack[-1]
                if topVal > abs(a):
                    break
                elif topVal < abs(a):
                    stack.pop()
                    continue
                else:
                    stack.pop() # dont append since we cancel out both vals
                    break
            else:
                stack.append(a)
        
        return stack