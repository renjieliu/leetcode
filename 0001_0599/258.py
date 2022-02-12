class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res >= 10:
            num = res
            curr = 0
            while num > 0: #add the current number digits
                curr += num%10 
                num //= 10
            res = curr # if curr is >=10, the iteration goes on. if not, just return the res
        return res



# previous approach

# class Solution:
#     def addDigits(self, num: int) -> int:
#         def helper(s):
#             return sum([int(a) for a in list(s)])
        
#         s = str(num)
#         while len(s) > 1 :
#             s = str(helper(s))
#         return int(s)



# previous approach

# def add(num):
#     x=list(str(num))
#     sum = 0
#     for i in range(0, len(x)):
#         sum+=int(x[i])

#     return sum


# def addDigits(num):
#     """
#     :type num: int
#     :rtype: int
#     """
#     t = add(num)
#     while t >= 10:
#         t=add(t)
#     else:
#         return t

# print(addDigits(38))


