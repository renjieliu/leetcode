class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        else: #the last file can be full or partial. full = full(k-1) + full(k-2). Partial = full(k-2) + partial(k-1)
            full_prev = 1 
            full_curr = 2 
            partial = 1
            for i in range(3, n+1):
                t = full_curr
                full_curr = full_prev + full_curr + 2*partial #partial can be 2 ways to put
                partial = partial + full_prev 
                full_prev = t 
            return full_curr % (10**9+7)
        

    