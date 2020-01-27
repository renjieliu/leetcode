class Solution:
    def filterRestaurants(self, restaurants: 'List[List[int]]', veganFriendly: int, maxPrice: int, maxDistance: int) -> 'List[int]':
        t = []
        for r in restaurants:
            if r[2] == (r[2] if veganFriendly ==0 else veganFriendly) and r[3] <= maxPrice and r[4] <= maxDistance:
                t.append(r)
        t.sort(key=lambda x: x[0], reverse = True)
        t.sort(key = lambda x: x[1], reverse = True) # from Python doc, when multiple items have the same key, original order is kept.
        output = []
        for i in t:
            output.append(i[0])
        return output