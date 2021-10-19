class Solution:
    def findTheDistanceValue(self, arr1: 'List[int]', arr2: 'List[int]', d: int) -> int:
        output = 0
        for a in arr1:
            find = 0
            for b in arr2:
                if abs(a-b) <= d:
                    find = 1
                    break
            if find == 0 :
                output+=1
        return output