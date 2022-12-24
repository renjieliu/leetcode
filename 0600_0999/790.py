class Solution:
    def numTilings(self, n: int) -> int: # O( N | 1 )
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
        



# previous solution

# class Solution:
#     def numTilings(self, n: int) -> int:
#         if n <= 2:
#             return n
#         else:
#             full_prev = 1 #the way to lay the prev tiling 
#             full_curr = 2 #the ways to lay the current tilings
#             partial_prev = 1 #the ways to lay the prev tiling in partial.
#             for i in range(3, n+1):
#                 t = full_curr 
#                 full_curr = full_prev + full_curr + 2*partial_prev #there are 2 directions to lay the partial.
#                 partial_prev = partial_prev + full_prev #either (partial_prev+ one full) or (full+ one partial)
#                 full_prev = t
#             return full_curr % (10**9+7)



# previous approach
# class Solution:
#     def numTilings(self, n: int) -> int:
#         if n <= 2:
#             return n
#         else: #the last file can be full or partial. full = full(k-1) + full(k-2). Partial = full(k-2) + partial(k-1)
#             full_prev = 1 
#             full_curr = 2 
#             partial = 1
#             for i in range(3, n+1):
#                 t = full_curr
#                 full_curr = full_prev + full_curr + 2*partial #partial can be 2 ways to put
#                 partial = partial + full_prev 
#                 full_prev = t 
#             return full_curr % (10**9+7)
        

    