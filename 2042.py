class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        curr = -1 
        for w in s.split(' '):
            if 48 <= ord(w[0]) <= 57:
                if int(w) > curr:
                    curr=int(w)
                else:
                    return False
        return True
    
