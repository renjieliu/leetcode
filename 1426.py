class Solution:
    def countElements(self, arr: 'List[int]') -> int:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1
        output = 0
        for k in hmp.keys():
            if k + 1 in hmp:
                output += hmp[k]
        return output



# below is the solution for O(N)
#
# class Solution:
#     def countElements(self, arr: 'List[int]') -> int:
#       return sum(map(lambda x: 1 if x+1 in arr else 0, arr))


