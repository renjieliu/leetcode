# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(arr, node, idx, find):
            if node.val == find:
                arr.append(idx)
                arr.append(-1)
            else:
                arr.append(idx)
                if node.left:
                    helper(arr, node.left, idx*2+1, find)
                if arr[-1] != -1 and node.right: # if found , no need to proceed
                    helper(arr, node.right, idx*2+2, find)
        arr_p = []
        arr_q = []
        helper(arr_p, root, 0, p.val)
        helper(arr_q, root, 0, q.val)

        #         print(arr_p, arr_q)

        arr_p.pop() #take out the -1 at the end of the arr, it was used to flag the number is found
        arr_q.pop()

        p_ancester = [arr_p[-1]]
        while p_ancester[-1] > 0:
            p_ancester.append((p_ancester[-1]-1)//2) #parent index is (curr-1)//2

        q_ancester = [arr_q[-1]]
        while q_ancester[-1] > 0:
            q_ancester.append((q_ancester[-1]-1)//2)

        targetIndex = max(set(p_ancester) & set(q_ancester)) #find the max common parent index

        def find(output, node, currIndex, targetIndex): # retrieve the node
            if currIndex == targetIndex:
                output[0] = node
            else:
                if node.left:
                    find(output, node.left, currIndex*2+1, targetIndex)
                if node.right:
                    find(output, node.right, currIndex*2+2, targetIndex)

        output = [None]
        find(output, root, 0, targetIndex)
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
#         def flat(output, curr, node, target):
#             if node.val == target:
#                 output.append(curr + [node])
#             else:
#                 if node.left:
#                     flat(output, curr + [node], node.left, target)
#                 if node.right:
#                     flat(output, curr + [node], node.right, target)
#
#         if root == None: return None
#         output = []  # there will be 2 paths in the output, 1 for p, 1 for q.
#         flat(output, [], root, p.val)
#         flat(output, [], root, q.val)
#         while output[0] and output[1] and output[0][0] == output[1][0]:  # find the last common predecessor
#             t = output[0].pop(0)
#             output[1].pop(0)
#         return t
