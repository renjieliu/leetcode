class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool: # O( N | N )
        loc = defaultdict(lambda : [])
        for i, n in enumerate(nums): # record all the number locations in the loc
            loc[n].append(i)
        
        for key, arr in loc.items(): # Check if there're 2 adjacent loc with dist <= k
            if len(arr) > 1:
                for i in range(1, len(arr)):
                    if arr[i] - arr[i-1] <= k:
                        return True
        return False
        
        


# previous solution

# def containsNearbyDuplicate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     map = {}
#     for i in range(0, len(nums)):
#         if nums[i] in map:
#             map[nums[i]].append(i)
#         else:
#             map[nums[i]] = []
#             map[nums[i]].append(i)

#     for v in map.values():
#         if len(v) <2:
#             continue
#         else:
#             for i in range(1, len(v)):
#                 if v[i] - v[i-1] <= k:
#                     return True

#     return False



# print(containsNearbyDuplicate([1,0,1,1], 1))
# print(containsNearbyDuplicate([1,2,3,1],3))
# print(containsNearbyDuplicate([1,2,1],0))
# print(containsNearbyDuplicate([],9))


