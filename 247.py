class Solution:
    def findStrobogrammatic(self, n: int) -> 'List[str]':
        def combo(A, B):
            output = []
            for a in A:
                for b in B:
                    output.append(a + b)
            return output

        if n == 1:
            return ['1', '8', '0']
        else:
            pool = ['1', '8', '0', '6', '9']
            temp = ['']
            i = 0
            while i < n // 2:
                temp = combo(pool, temp)
                i += 1
            output = []
            if n % 2 == 0:
                for t in temp:
                    if t[0] != '0':
                        output.append(t + t[::-1].replace('6', '7').replace('9', '6').replace('7',
                                                                                              '9'))  # reverse the first half, 9 to 6, and 6 to 9
                return output
            else:
                for p in ['1', '8', '0']:
                    for t in temp:
                        if t[0] != '0':
                            output.append(t + p + t[::-1].replace('6', '7').replace('9', '6').replace('7',
                                                                                                      '9'))  # reverse the first half, plus 0, 1, 8, and flip 6 and 9
                return output





