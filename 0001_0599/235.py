# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def explore(find, path, node, v, idx):
            if node.val == v:
                path.append(idx)
                find.append(1)
            else:
                path.append(idx)
                if node.left:
                    explore(find, path, node.left, v, idx*2+1)
                if len(find) == 0 and node.right:
                    explore(find, path, node.right, v , idx*2+2)
        a = []
        explore([], a, root, p.val, 0)
        b = []
        explore([], b, root, q.val, 0)
        p_a = [a[-1]]
        p_b = [b[-1]]

        i = a[-1] #to find all the parent node, including itself
        while i > 0:
            i = (i-1)//2
            p_a.append(i)

        i = b[-1]
        while i > 0:
            i = (i-1)//2
            p_b.append(i)

        p_a = p_a[::-1]
        p_b = p_b[::-1]

        # print(a, b, p_a, p_b)

        lca = None
        while p_a and p_b and p_a[0] == p_b[0]:
            lca = p_a.pop(0)
            p_b.pop(0)

        output = []
        def dfs(output, node, lca, idx):
            if idx == lca:
                output.append(node)
            else:
                if node.left:
                    dfs(output, node.left, lca, idx*2+1)
                if node.right and len(output) == 0:
                    dfs(output, node.right, lca, idx*2+2)
        dfs(output, root, lca, 0)
        return output[0]



# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def flat(node, output, curr, target):
#             if node.val == target:
#                 output.append(curr+[node])
#             else:
#                 if node.left: flat(node.left, output, curr+[node], target)
#                 if node.right: flat(node.right, output, curr+[node], target)
#         if root == None: return None
#         output = []
#         flat(root, output, [], p.val)
#         flat(root, output, [], q.val)
#         while output[0] and output[1] and output[0][0] == output[1][0]:
#             t = output[0].pop(0)
#             output[1].pop(0)
#         return t