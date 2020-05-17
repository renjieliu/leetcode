class Solution:
    def simplifiedFractions(self, n: int) -> 'List[str]':
        def gcd(n1, n2):
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1

        if n == 1: return []
        output = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if gcd(i, j) == 1:
                    output.append(str(i) + "/" + str(j))
        return output
