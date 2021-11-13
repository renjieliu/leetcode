class Solution:
    def numTrees(self, n: int) -> int:
        hmp = {0:1, 1:1} #to faciliate calc empty left subtree, put 0 as 1
        for total_nodes in range(2, n+1):
            curr = 0
            for left_node_count in range(total_nodes): # total = left * right
                right_node_count = hmp[total_nodes-1-left_node_count] # -1 is the current root
                curr+= hmp[left_node_count] * right_node_count
            hmp[total_nodes] = curr
        return hmp[n]
                

# previous approach
# class Solution:
#     def numTrees(self, n: int) -> int:
#         if n <= 1:
#             return n
#         else:
#             dp = [1, 1]
#             for i in range(2, n + 1):
#                 curr = 0
#                 for j in range(1, i + 1):
#                     curr += dp[j - 1] * dp[i - j]
#                 dp.append(curr)
#             return dp[-1]




