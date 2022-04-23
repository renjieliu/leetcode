class Solution:
    def minimumRounds(self, tasks: 'List[int]') -> int: # O(N | N)
        hmp = defaultdict(lambda:0) # count the occurrence of each digit
        for t in tasks:
            hmp[t] += 1 
        
        cnt = 0 
        for k, v in hmp.items():
            if v == 1:
                return -1
            cnt += v // 3 + (v % 3 > 0)  # if v % 3 == 0 return v//3. v%3==1: return (v-2)//3 + rem//2. if v%3 ==2, v//3+rem//2
        return cnt 
    
  
