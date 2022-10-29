class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int: # O( N | 1 )
        gap_zero = 0 # count of 0 in between
        while nums and nums[0] == 0: # take out the leading 0
            nums.pop(0)
            gap_zero += 1        
        
        if nums == []: # the only element in the nums is 0s 
            return 1
        output = 0 
        prev_cnt = 0 # length of prev segment of 1  
        
        curr_cnt = 1 # curr_segment of 1 
        nums.pop(0) 
        
        while nums:
            n = nums.pop(0)
            if n == 1:
                curr_cnt += 1 # keep adding to the current segment
            elif n == 0 : 
                if curr_cnt > 0 : # meeting the first 0 after one segment 
                    if gap_zero <= 1: #calculate the prev 2 segments
                        output = max(output, curr_cnt + prev_cnt + (gap_zero == 1)) # +1 to included the flipped 0
                    else: # just compare the current 1 segment 
                        output = max(output, curr_cnt + 1) # flip one leading 0 to 1 
                    gap_zero = 0
                    prev_cnt = curr_cnt
                    curr_cnt = 0
                gap_zero += 1  
                
        if curr_cnt > 0: # trailing 1 can connect with prev one segment or not, and see if there's a 0 to flip
            if gap_zero <= 1:
                output = max(output, curr_cnt + prev_cnt + (gap_zero == 1))
            else:
                output = max(output, curr_cnt + 1)
        
        else: # flip first of the trailing 0 to 1
            output = max(output, prev_cnt+1)
        return output
    

                    
                    
            

            
