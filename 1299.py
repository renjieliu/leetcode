class Solution:
    def replaceElements(self, arr: 'List[int]') :
        m = arr[-1]
        output = [-1]
        for i in range(len(arr)-2,-1,-1):
            output.insert(0,m)
            m = max(m, arr[i])
        return output