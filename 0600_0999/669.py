# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: 'Optional[TreeNode]', low: int, high: int) -> 'Optional[TreeNode]': #O(N | 1)
        def helper(node, lo, hi, prev):
            if node:
                # print(node.val, prev)
                if lo <= node.val <= hi: # keep it, and add to the prev valid node
                    if node.val < prev.val:
                        prev.left = node
                    else:
                        prev.right = node
                        # print('prev', prev)
                else:
                    if node.val < prev.val and prev.left == node: #take it out from the tree
                        prev.left = None
                    elif node.val > prev.val and prev.right == node:
                        prev.right = None
                    
                helper(node.left, lo, hi, node if lo <= node.val <= hi else prev )
                helper(node.right, lo, hi, node if lo <= node.val <= hi else prev )
                
        newRoot = TreeNode(-float('inf')) #dummy node.
        helper(root, low, high, newRoot)
        # print(newRoot)
        return newRoot.right #the dummy start node.val is -float('inf'), the so new root would be newRoot.right
    
   




# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
#         def flat(output, node, low, high):
#             if low<=node.val<=high:
#                 output.append(node.val)
#             if node.left:
#                 flat(output, node.left, low, high)
#             if node.right:
#                 flat(output, node.right, low, high)

#         def buildTree(arr, node, low, high):
#             if arr and low <= arr[0] <= node.val:
#                 node.left = TreeNode(arr[0])
#                 arr.pop(0)
#                 buildTree(arr, node.left, low, node.val)
#             if arr and node.val <= arr[0] <= high :
#                 node.right = TreeNode(arr[0])
#                 arr.pop(0)
#                 buildTree(arr, node.right, node.val, high)


#         output = []
#         flat(output, root, low, high)
#         if output == []:
#             return None
#         else:
#             start = TreeNode(output.pop(0))
#             node = start
#             buildTree(output, node, low, high)
#             return start










