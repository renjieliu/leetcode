class Solution:
    def kInversePairs(self, n: int, k: int) -> int: #RL 20220716: copied solution, O( N*k | N*k )
        mod = 10**9 + 7
        ds = [0] + [1] * (k + 1)
        for n in range(2, n+1):
            new = [0]
            for k in range(k+1):
                v = ds[k+1]
                v -= ds[k-n+1] if k >= n else 0
                new.append( (new[-1] + v) % mod )
            ds = new
        return (ds[k+1] - ds[k]) % mod
    
    
    
# previous solution

# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         mod = 10**9 + 7
#         ds = [0] + [1] * (k + 1)
#         for n in range(2, n+1):
#             new = [0]
#             for k in range(k+1):
#                 v = ds[k+1]
#                 v -= ds[k-n+1] if k >= n else 0
#                 new.append( (new[-1] + v) % mod )
#             ds = new
#         return (ds[k+1] - ds[k]) % mod




