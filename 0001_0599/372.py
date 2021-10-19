class Solution:
    def superPow(self, a: int, b: 'List[int]') -> int:  # (a^10)%n =  (a%n*a%n *...a%n)%n
        if b == []:
            return 1  # a^0%1337 == 1%1337 = 1
        else:
            base = a
            output = 1
            n = 1337
            for i in b[::-1]:  # foreach i in the array backwards
                temp = 1
                for j in range(10):  # for each i, calculate the base^i.
                    if j == i:
                        output = (output * temp) % n  #
                    temp = (base * temp) % n  # a^1%n, a^2%n....a^10%n

                base = temp  # make a as the current base

        return output
