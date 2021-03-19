class Solution:
    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> bool:
        def dfs(seen, arr, curr):
            for c in arr[curr]:
                if c not in seen:
                    seen.add(c)
                    dfs(seen, arr, c)
        seen = set([0])
        dfs(seen, rooms,0)
        #print(seen)
        return len(seen) == len(rooms)
