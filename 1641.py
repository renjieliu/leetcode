class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        elif n == 2:
            return 15
        else:
            curr = 15
            prevA = 5
            prevE = 4
            prevI = 3
            prevO = 2
            for l in range(3, n + 1):
                a = curr
                e = a - prevA
                i = e - prevE
                o = i - prevI
                u = 1
                # print(a,e,i,o,u)
                prevA = a
                prevE = e
                prevI = i
                prevO = o
                curr = sum([a, e, i, o, u])

            return curr
