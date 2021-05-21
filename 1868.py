class Solution:
    def findRLEArray(self, encoded1: 'List[List[int]]', encoded2: 'List[List[int]]') -> 'List[List[int]]':
        output = []
        a = encoded1
        b = encoded2
        i = j = 0
        while i < len(a) and j < len(b):  # using pointers to speed up.
            if a[i][1] < b[j][
                1]:  # advance the i, if current a[i][1] is less than the current b[j][i], it means, b[j][i] has some left, to calculate with the next a item
                output.append([a[i][0] * b[j][0], a[i][1]])
                b[j][1] -= a[i][1]
                i += 1
            elif a[i][1] == b[j][1]:
                output.append([a[i][0] * b[j][0], a[i][1]])
                i += 1
                j += 1
            elif a[i][1] > b[j][1]:
                output.append([a[i][0] * b[j][0], b[j][1]])
                a[i][1] -= b[j][1]
                j += 1
            while len(output) > 1 and output[-2][0] == output[-1][
                0]:  # merge with previous array, if the product is same
                output[-2][1] += output[-1][1]
                output.pop(-1)
        return output



