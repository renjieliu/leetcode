class Solution:
    def isUgly(self, n: int) -> bool: # O( logN | 1 )
        if n <= 0:
            return False 
        
        while n > 0: # keep dividing n, until cannot be devided by 2, 3, 5
            if n % 2 == 0:
                n //= 2 
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else: 
                break
        
        return n in (1,2,3,5)
    



# previous solution

# def is_Prime(n):
#     if n==2:
#         return 1
#     for i in range(2, int(n**0.5)  +1):
#         if n%i == 0:
#             return 0
#     return 1


# def isUgly(num):
#     """
#     :type num: int
#     :rtype: bool
#     """
#     if is_Prime(num):
#         return False

#     else:
#         cnt = 0
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 #print(i, end = ",")
#                 if is_Prime(i) == 1 and i !=2 and i!=3 and i!=5:
#                     return False
#                 if is_Prime(num/i) == 1 and (num/i) !=2 and (num/i)!=3 and (num/i) !=5:
#                     return False
#         return True


# print(isUgly(6))
# print(isUgly(28))
# print(isUgly(30))
# print(isUgly(91))
# print(isUgly(2147483647))


