# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def flat(path, node):
            path.append(str(node.val))
            if node.next!=None:
                node = node.next
                flat(path, node)
    
        path = []
        flat(path, head)
        path = ''.join(path)
        #print(path)
        def dfs(pool, node, currPath):
            if node.left==None and node.right ==None:
                pool.append(currPath+str(node.val) )
                return 1 
            else:
                if node.left!= None:
                    t = currPath+str(node.val)
                    dfs(pool, node.left, t)
                if node.right!=None:
                    t = currPath+str(node.val)
                    dfs(pool, node.right, t)
        pool = [] 
        dfs(pool,root, "" )
        #print(pool, path)
        for p in pool:
            if path in p:
                return True
        return False
        
        
        