class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lo = hi = dig = spec = 0
        if len(password) < 8:
            return False 
        for i in range(len(password)):
            curr = ord(password[i])
            if 97 <= curr <= 122:  #lower case character
                lo = 1 
            elif 65 <= curr <= 90: #upper case characrer
                hi = 1
            elif 48<=curr <= 57: # digit
                dig = 1
            elif password[i] in "!@#$%^&*()-+": #special character
                spec = 1 
            
            if i > 0 and password[i] == password[i-1]: # same as the prev character
                return False
        
        return lo * hi * dig * spec != 0

    
