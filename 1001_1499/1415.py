class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        stk = ['a', 'b', 'c']
        hmp = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}
        total_initial = 3 * (2 ** (n - 1))
        if k > total_initial:
            return ""
        else:
            each = total_initial // 3  # spaces each letter takes
            ceiling = lambda x: int(x) if x == int(x) else int(x) + 1  # current k is within the Nth segment
            segment = ceiling(k / each)
            firstLetter = stk[segment - 1]  # get the first letter
            output = firstLetter
            k = k - (k // each) * each
            n -= 1
            while n > 0:  # same idea as the first letter, to get the follow letters
                currTotal = 2 ** n
                each = currTotal // 2
                segment = ceiling(k / each)
                output += hmp[output[-1]][segment - 1]
                k = k - (k // each) * each
                n -= 1

            return output