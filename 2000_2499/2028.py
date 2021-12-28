class Solution:
    def missingRolls(self, rolls: 'List[int]', mean: int, n: int) -> 'List[int]':
        currTotal = sum(rolls)
        m = len(rolls)
        diff = mean*(m+n) - currTotal
        if diff < n or diff > 6*n:
            return []
        else:
            output = [diff // n] * n 
            rem = diff - sum(output) #first rem items need to add 1 each
            for i in range(rem):
                output[i] +=1
            return output

    
