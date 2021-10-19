class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = str(N)
        check = ""
        for x in s:
            if x in ['0', '1', '8']:
                check += x
            elif x == '6':
                check += '9'
            elif x == '9':
                check += "6"
            else:
                return False
        check = check[::-1]
        if int(check) == N:
            return False
        else:
            return True
