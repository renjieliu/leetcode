class Solution:
    def minInsertions(self, s: str) -> int:
        stk_left = 0
        stk_right = 0
        output = 0
        for c in s:
            if c == ")":
                stk_right += 1
                if stk_right == 2:
                    if stk_left > 0:
                        stk_left -= 1
                        stk_right = 0
                    elif stk_left == 0:
                        output += 1  # add a left
                        stk_right = 0
            elif c == "(":
                if stk_right == 1:
                    if stk_left == 0:
                        output += 2  # add a right and left
                        stk_right = 0
                    else:
                        output += 1  # add a right
                        stk_left -= 1
                        stk_right = 0
                stk_left += 1

        if stk_left > 0:
            if stk_right == 0:
                output += 2 * stk_left
            else:
                output += 2 * (stk_left - 1) + 1
        else:
            if stk_right == 1:
                output += 2

        return output


