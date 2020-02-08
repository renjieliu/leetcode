class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num ==0 : return 0
        else:
            cnt = 0
            while num > 1:
                cnt += 1+ (num%2) #if odd, then add 2, if even, add 1
                num = num>>1
            return cnt +1 #cnt==1, and need one more step to turn to 0

#Trivial solution
# cnt = 0
# while num != 0 :
#     if num%2==0:
#         num/=2
#     else:
#         num-=1
#     cnt +=1
# return cnt