class Solution:
    def kInversePairs(self, n: int, k: int) -> int: #RL 20220716: copied solution, O( N*k | N*k )
        mod = 10**9 + 7
        
        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
                g[j] %= mod
            f = g
        
        return f[k]

    
#     def kInversePairs(self, n: int, k: int) -> int:
#         mod = 10**9 + 7
        
#         f = [1] + [0] * k
#         for i in range(1, n + 1):
#             g = [0] * (k + 1)
#             for j in range(k + 1):
#                 g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
#                 g[j] %= mod
#             f = g
        
#         return f[k]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-inverse-pairs-array/solution/kge-ni-xu-dui-shu-zu-by-leetcode-solutio-0hkr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# previous solution

# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int: #RL 20220716: copied solution, O( N*k | N*k )
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




