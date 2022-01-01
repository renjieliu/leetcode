class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        else:
            i = 1
            while True:
                if i % k == 0:
                    return len(str(i))
                i = i*10+1



# previous approach

# class Solution:
#     def smallestRepunitDivByK(self, K: int) -> int:
#         if K % 2 == 0 or K %5 == 0:
#             return -1
#         else: 
#             if K == 1 :
#                 return 1
#             else:
#                 N = 11
#                 while N%K != 0:
#                     N = N*10+1
#                 return len(str(N))



# previous approach

# def smallestRepunitDivByK(K: int):
#     if int(str(K)[-1]) in [2, 4, 5, 6, 8, 0]:
#         return -1
#     elif K == 1:
#         return 1
#     else:
#         temp = 11
#         while temp%K != 0:
#             temp = temp*10+1

#         return len(str(temp))

# print(smallestRepunitDivByK(1))
# print(smallestRepunitDivByK(2))
# print(smallestRepunitDivByK(19921))
# print(smallestRepunitDivByK(73))
# print(smallestRepunitDivByK(3))
# print(smallestRepunitDivByK(7))
# print(smallestRepunitDivByK(5))
# print(smallestRepunitDivByK(9))
# print(smallestRepunitDivByK(15))

