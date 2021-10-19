class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        stk_str = []
        stk_num = []
        nums = [str(_) for _ in range(10)]
        in_num = 0  # the number needs to be appended to the previous
        for c in s:
            if c in nums:
                if in_num == 0:
                    stk_num.append("")
                    in_num = 1
                stk_num[-1] += c

            elif c == "[":
                in_num = 0
                stk_str.append("")

            elif c == "]":
                curr = stk_str.pop() * int(stk_num.pop())
                if stk_str:
                    stk_str[-1] += curr
                else:
                    output += curr
            else:
                if stk_str:
                    stk_str[-1] += c
                else:
                    output += c

        output += stk_str[-1] if stk_str else ""
        return output







