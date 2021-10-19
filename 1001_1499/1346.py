class Solution:
    def checkIfExist(self, arr: 'List[int]') -> bool:
        arr.sort()
        i = 0
        while i < len(arr):
            curr = arr[i]
            for x in arr[:i] + arr[i+1:]:
                if x==2*curr:
                    return True
                elif x>2*curr:
                    break
            i+=1
        return False