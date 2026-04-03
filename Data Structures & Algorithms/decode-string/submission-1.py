class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (previous_string, repeat_count)
        curr_str = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)

            elif c == "[":
                # Save current context and start fresh
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif c == "]":
                prev_str, repeat = stack.pop()
                curr_str = prev_str + curr_str * repeat

            else:  # letter
                curr_str += c

        return curr_str