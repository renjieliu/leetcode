class Solution:
    def maximumBags(self, capacity: 'List[int]', rocks: 'List[int]', additionalRocks: int) -> int: #O(nlogn | n)
        delta = sorted([c-r for c, r in zip(capacity, rocks)])  # find how many space left for each bag
        for i in range(len(delta)): # fill the smallest delta first
            if additionalRocks >= delta[i]:
                additionalRocks -= delta[i]
                delta[i] = 0
                if additionalRocks <= 0:
                    break
            else: # cannot fill the rest bags, no need to continue
                break
        # print(delta)
        return len([d for d in delta if d == 0])
            
            
