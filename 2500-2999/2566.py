class Solution:
    def minMaxDifference(self, num: int) -> int: # O( logN | 1 )
        num = str(num)
        mi = int(num.replace(num[0],"0")) # map the first number to 0
        mx = int(num)
        for i in range(len(num)): # map the first non-9 to 9
            if num[i] != "9":
                mx = int(num.replace(num[i], "9"))
                break
        
        return mx-mi
                

