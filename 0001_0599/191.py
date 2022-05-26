class Solution:
    def hammingWeight(self, n: int) -> int: #O(K | 1), K is the bit length of n 
        cnt = 0 
        while n > 0:
            cnt += n&1 #if 
            n >>= 1
        return cnt
    


# previous solution


# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         cnt = 0
#         while n != 0:
#             if n%2 ==1:
#                 cnt +=1
#             n = n >> 1
#         return cnt

# previous approach
# def hammingWeight(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     sum = 0
#     for i in bin(n).replace("0b",""):
#         sum += int(i)
#     return sum
#
# print(hammingWeight(11))
# print(hammingWeight(128))
#
