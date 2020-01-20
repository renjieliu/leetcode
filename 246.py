class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        temp = ""
        for n in num:
            if n in ['0','1','8']:
                temp+=n
            elif n == '6':
                temp+='9'
            elif n == '9':
                temp+='6'
            else:
                return False
        return True if temp[::-1] == num else False
