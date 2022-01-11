# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: 'Optional[TreeNode]') -> int:
        def calc(arr):
            output = 0
            for i in range(len(arr)-1, -1, -1): #calc the binary to 10-based, from right to left 
                power = len(arr)-1-i
                output += arr[i]*(2**power)
            # print(arr, output)
            return output 
        
        def helper(output, arr, node):
            if node.left == node.right == None:
                output[0] += calc(arr + [node.val])
            if node.left:
                helper(output, arr + [node.val], node.left)
            if node.right:
                helper(output, arr + [node.val], node.right)
        
        output = [0]
        helper(output, [], root)
        
        return output[0]
    
    




# previous approach

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         def flat(node, path, output):
#             if node.left == node.right == None:
#                 output.append(path + [str(node.val)])
#             else:
#                 if node.left:
#                     flat(node.left, path + [str(node.val)], output)
#                 if node.right:
#                     flat(node.right, path + [str(node.val)], output)

#         if root == None:
#             return 0
#         else:
#             output = []
#             flat(root, [], output)
#             return sum([int(''.join(x), 2) for x in output])


# previous approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         def BintoDec(n):
#             output = 0
#             power = 0
#             for i in range(len(n) - 1, -1, -1):
#                 output += n[i] * (2 ** power)
#                 power += 1
#             return output
#
#         def flat(output, node, curr):
#             if node.left == node.right == None:
#                 output.append(curr + [node.val])
#             else:
#                 if node.left:
#                     flat(output, node.left, curr + [node.val])
#                 if node.right:
#                     flat(output, node.right, curr + [node.val])
#
#         output = []
#         if root == None:
#             return 0
#         else:
#             flat(output, root, [])
#             # print(output)
#             ans = 0
#             for o in output:
#                 ans += BintoDec(o)
#             return ans
#
#
#
