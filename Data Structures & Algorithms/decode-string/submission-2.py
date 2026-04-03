class Solution:
    def decodeString(self, s: str) -> str:
        # intuition: we want to first process whatever
        # is on the innermost brackets so we build up
        # a stack that way, and then we pop all the shit out
        # of the satck s.t. we can reconstruct the multiplier
        # of the digit
        stack = []  # (previous_string, repeat_count)
        curr_str = ""
        curr_mult = 0

        for c in s:
            if c.isdigit():
                curr_mult = curr_mult * 10 + int(c)

            elif c == "[":
                # Save current context and start fresh
                stack.append((curr_str, curr_mult))
                curr_str = ""
                curr_mult = 0

            elif c == "]":
                prev_str, repeat = stack.pop()
                curr_str = prev_str + curr_str * repeat

            else:  # letter
                curr_str += c

        return curr_str