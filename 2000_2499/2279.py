class Solution:
    def maximumBags(self, capacity: 'List[int]', rocks: 'List[int]', additionalRocks: int) -> int: # O( NlogN | N )
        diff = sorted(a-b for a, b in zip(capacity, rocks)) # find the deficit of current rocks and full capacity
        cnt = 0 
        while diff and diff[0] == 0:  #count the ones already full 
            cnt += 1
            diff.pop(0)
        while diff and additionalRocks >= diff[0]: # put rocks to the smallest deficit
            cnt += 1
            additionalRocks -= diff.pop(0)
        
        return cnt



# previous solution

# class Solution:
#     def maximumBags(self, capacity: 'List[int]', rocks: 'List[int]', additionalRocks: int) -> int: # O( NlogN | N )
#         diff = sorted(abs(a-b) for a, b in zip(capacity, rocks)) # find the deficit of current rocks and full capacity
#         cnt = 0 
#         while diff and diff[0] == 0:  #count the ones already full 
#             cnt += 1
#             diff.pop(0)
#         while diff and additionalRocks >= diff[0]: # put rocks to the smallest deficit
#             cnt += 1
#             additionalRocks -= diff.pop(0)
        
#         return cnt



# previous solution

# class Solution:
#     def maximumBags(self, capacity: 'List[int]', rocks: 'List[int]', additionalRocks: int) -> int: #O(nlogn | n)
#         delta = sorted([c-r for c, r in zip(capacity, rocks)])  # find how many space left for each bag
#         for i in range(len(delta)): # fill the smallest delta first
#             if additionalRocks >= delta[i]:
#                 additionalRocks -= delta[i]
#                 delta[i] = 0
#                 if additionalRocks <= 0:
#                     break
#             else: # cannot fill the rest bags, no need to continue
#                 break
#         # print(delta)
#         return len([d for d in delta if d == 0])
            
            
