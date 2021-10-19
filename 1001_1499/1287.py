class Solution:
    def findSpecialInteger(self, arr: 'List[int]') -> int:
        if len(arr) == 1:
            return arr[0]
        else: 
            cnt = 0
            threshold = len(arr)//4 
            for i in range(1, len(arr)):
                if arr[i] == arr[i-1]:
                    cnt +=1
                    if cnt > threshold:
                        return arr[i]
                else:
                    cnt = 1
                
