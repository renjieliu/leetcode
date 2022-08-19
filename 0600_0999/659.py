class Solution:
    def isPossible(self, nums: 'List[int]') -> bool:
        hmp = defaultdict(lambda:0)
        for n in nums: # count the occurrence of each number in the nums 
            hmp[n] += 1 
        arr = sorted(hmp.keys()) 
        while arr:
            head = arr.pop(0) # check current head of the array
            while hmp[head] > 0 : #keep add current number to the group, until exhausted
                prev_cnt = hmp[head] # occurrence of the previous number
                L = 1 #current number length count
                hmp[head] -= 1
                curr = head
                while hmp[curr + 1] >= prev_cnt:  # stop when the occurrence decreases
                    curr += 1 
                    L += 1 
                    prev_cnt = hmp[curr]
                    hmp[curr] -= 1 
                if L < 3:
                    return False
        return True
    
