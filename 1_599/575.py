class Solution:
    def distributeCandies(self, candyType: 'List[int]') -> int:
        return int(min(len(set(candyType)),  len(candyType)/2))


# previous approach
# def distributeCandies(candies):
#     """
#     :type candies: List[int]
#     :rtype: int
#     """
#     map = {}
#     total = 0
#     for i in candies:
#         total += 1
#         if i not in map:
#             map[i] = 1
#
#     if len(map.keys()) >= len(candies) / 2:
#         return int(len(candies) / 2)
#     else:
#         return len(map.keys())
#
# print(distributeCandies([1,1,2,2,3,3]))
# print(distributeCandies([1,1,2,3]))