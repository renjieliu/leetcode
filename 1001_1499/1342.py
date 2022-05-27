class Solution:
    def numberOfSteps(self, num: int) -> int: #O(K | 1), k is the bit length of num
        cnt = 0 
        while num > 1: #all the number will be 1, and from 1, just add 1 step to the output
            cnt += 1 + (num & 1)
            num >>= 1 
        return cnt + num # 1 if num != 0 else 0 , num will always be 1 or 0 after prev iteration
        
    


# previous solution

# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         cnt = 0
#         while num!=0:
#             if num %2 != 0 :
#                 num -= 1
#                 cnt += 1
#                 if num == 0 :
#                     return cnt
#             num = num >> 1
#             cnt += 1
#         return cnt



# previous solution 

# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         if num ==0 : return 0
#         else:
#             cnt = 0
#             while num > 1:
#                 cnt += 1+(num%2)
#                 num = num>>1
#             return cnt +1 #cnt==1, and need one more step to turn to 0 


