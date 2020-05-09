#binary search approach
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        e = num
        while s <= e:
            mid = s - (s-e)//2
            if num == mid ** 2:
                return True
            else:
                if mid**2 > num:
                    e = mid -1
                elif mid**2 < num:
                    s = mid +1
        return False




# old, Newton square root approach
# def isPerfectSquare(num):
#     """
#     :type num: int
#     :rtype: bool
#     """
#     x = 1
#     t=num
#     while x < 100 :
#         t = 0.5*(t + num/t)
#         x+=1
#     if t-t//1 ==0 :
#         return True
#     else:
#         return False


# print(isPerfectSquare(15))

