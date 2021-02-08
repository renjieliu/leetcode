class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if len(preorder.replace(",", "")) == 2:  # the string lenth is 2, then it's not a BT
            return False
        elif preorder == "#":
            return True
        else:
            num_stk = []
            for i in range(len(preorder.split(","))):
                p = preorder.split(",")[i]

                if i > 0 and num_stk == []:  # The num_stk has been exhausted, and there's still chars left
                    return False
                else:
                    if p != "#":
                        num_stk.append([p, 0])
                    elif p == "#":
                        if len(num_stk) > 0:
                            num_stk[-1][1] += 1
                        else:
                            return False  # if no number exists, and it reads a # from the string, it will be invalid.
                    if len(num_stk) > 0:
                        while num_stk[-1][1] == 2:
                            num_stk.pop()
                            if num_stk == []:
                                break
                            else:
                                num_stk[-1][1] += 1

            if num_stk == []:
                return True

            return False