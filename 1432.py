class Solution:
    def maxDiff(self, num: int) -> int:
        a = []
        b = []
        temp = str(num)
        for i in range(10):
            for j in range(10):
                t = temp.replace(str(i), str(j))
                if t[0] != "0":
                    a.append(int(t))
                    b.append(int(t))
        output = -float('inf')
        for i in a:
            for j in b:
                output = max(output, abs(j - i))
        return output


