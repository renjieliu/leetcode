class Solution:
    def minEatingSpeed(self, piles: 'List[int]', h: int) -> int:
        s = 1
        e = max(piles)
        output = float('inf')
        while s <= e:
            mid = (s+e)//2 
            total = sum([p//mid + (1 if p%mid else 0) for p in piles]) # hours needed to eat all the arr , with current speed v
            if total <= h:
                e = mid - 1
                output = min(output, mid)
            else:
                s = mid + 1 
        
        return output
            

  

# previous approach

# class Solution:
#     def minEatingSpeed(piles: 'List[int]', H: int) -> int:
#         if len(piles) == H:
#             return max(piles)
#         else:
#             # use binary search to find the number, range 1 to max(piles). #if none fits, return the best one that fits the criteria.
#             end = max(piles)
#             start = 1
#             output = end
#             while start <= end:
#                 mid = (start + end) // 2
#                 shadow = piles.copy()
#                 hours = 0
#                 i = 0
#                 while i < len(shadow):
#                     needed = shadow[i] % mid
#                     hours += shadow[i] // mid + (
#                         1 if needed != 0 else 0)  # need 1 more hour to finish the remaining of the pile.
#                     i += 1

#                 if hours == H:
#                     return mid

#                 elif hours > H:  # it does not fit
#                     start = mid + 1

#                 elif hours < H:  # it fits, but it can be improved
#                     output = min(output, mid)
#                     end = mid - 1

#             return output
