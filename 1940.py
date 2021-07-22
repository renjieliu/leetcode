class Solution:
    def longestCommomSubsequence(self, arrays: 'List[List[int]]') -> 'List[int]':
        def common(a, b):
            output = []
            while a and b:
                if a[0] == b[0]:
                    output.append(a[0])
                    a.pop(0)
                    b.pop(0)
                elif a[0] < b[0]:
                    a.pop(0)
                elif a[0] > b[0]:
                    b.pop(0)
            return output
        output = common(arrays.pop(0), arrays.pop(0))
        while arrays:
            output = common(arrays.pop(0), output)
        return output

