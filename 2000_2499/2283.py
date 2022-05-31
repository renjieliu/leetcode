class Solution:
    def digitCount(self, num: str) -> bool: #O(N | 1)
        arr = [0] * 10 # record the occurrence of each number
        for n in num:
            arr[ord(n)-ord('0')] += 1 
            
        for i, n in enumerate(num): # check if i appear n times
            if arr[i] != int(n):
                return False
        return True
    
    
