class Solution:
    def isDecomposable(self, s: str) -> bool:
        if len(s)%3 != 2:
            return False
        else:
            diff = 0
            start = s[0]
            curr = 1
            for c in s[1:]:
                if curr == 3:
                    start = c
                    curr = 1
                else:
                    if c == start:
                        curr += 1
                    else:
                        if curr == 2:
                            start = c
                            curr = 1
                            diff += 1
                            if diff > 1 :
                                return False
                        else:
                            return False

            return True
