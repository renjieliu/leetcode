class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        direction = None  # s1 break s2 or s2 to break s1
        while s1 and s2:
            if s1[0] == s2[0]:
                s1.pop(0)
                s2.pop(0)
            else:
                if s1[0] > s2[0]:
                    if direction == None:  # set s1 to break s2
                        direction = 1
                    elif direction != 1:
                        return False
                elif s2[0] > s1[0]:
                    if direction == None:  # set s2 to break s1
                        direction = 2
                    elif direction != 2:
                        return False
                s1.pop(0)
                s2.pop(0)
        return True

