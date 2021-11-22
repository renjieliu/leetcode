# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: 'Optional[TreeNode]', key: int) -> 'Optional[TreeNode]':
        def flat(arr, node, key): # flatten the target node
            if node.val != key:
                arr.append(node.val)
            if node.left: 
                flat(arr, node.left, key)
            if node.right: 
                flat(arr, node.right, key)
            
        def find(res, arr, node, key): #find the target node
            if node.val == key:
                res[0] = 1 
                flat(arr, node, key)
                
            if arr == []:
                if node.left:
                    find(res, arr, node.left, key)
                if node.right: 
                    find(res, arr, node.right, key)
        
        if root == None:
            return None
       
        arr = []
        res = [0]
        find(res, arr, root, key)
        # print(res)
        if res[0] == 0: # does not find the target value
            return root
        
        if arr == []:
            newNode = None
        else:
            arr.sort()
            newNode = TreeNode(arr[0]) #build new sub tree of the target node
            curr = newNode
            for a in arr[1:]:
                curr.right = TreeNode(a)
                curr = curr.right
            
        if root.val == key:
            return newNode
            
            
        def build(newNode, node, key): # plug the new sub tree to root
            if node.left:
                if node.left.val == key:
                    node.left = newNode 
                    return
                else:
                    build(newNode, node.left, key)
            if node.right:
                if node.right.val == key:
                    node.right = newNode 
                    return
                else:
                    build(newNode, node.right, key)
        
        build(newNode, root, key)
        return root
    
    


# previous approach 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         def helper(node, target):
#             if node == None: return None

#             if node.val == target:
#                 if node.left == node.right == None:
#                     return None
#                 elif node.left and node.right == None:
#                     return node.left
#                 elif node.right and node.left == None:
#                     return node.right
#                 else:
#                     curr = node.right
#                     while curr.left:
#                         curr = curr.left
#                     node.val = curr.val
#                     node.right = helper(node.right, curr.val)

#             elif node.val > target:
#                 node.left = helper(node.left, target)
#             elif node.val < target:
#                 node.right = helper(node.right, target)

#             return node

#         node = helper(root, key)

#         return node

