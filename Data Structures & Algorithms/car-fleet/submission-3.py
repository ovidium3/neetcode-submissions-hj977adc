class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # intuition: we must first sort the cars so that
        # we can process them accurately and use the stack
        # so that for each pairing, we calculate how much time it will take
        # the car to get to destination, THEN do the comparison on the stack
        # to try and merge the car with the one ahead of it.
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)