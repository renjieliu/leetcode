# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: 'Optional[TreeNode]', queries: 'List[int]') -> 'List[List[int]]': # O( NlogN | N )
        def flat(arr, node):
            arr.append(node.val)
            if node.left:
                flat(arr, node.left)
            if node.right:
                flat(arr, node.right)
            
        arr = []
        flat(arr, root)
        arr.sort()
        output = []

        def binFindMax(arr, v): # find the max(n) <= v
            if v < arr[0]: # nothing in the arr is < v
                return -1 
            s = 0 
            e = len(arr)-1 
            output = -1
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] == v:
                    return arr[mid]
                elif arr[mid] < v:
                    s = mid + 1 
                    output = arr[mid]
                else: 
                    e = mid - 1
            return output 
        
        def binFindMin(arr, v): # find the min(n) >= v
            if v > arr[-1]: # nothing in the arr is > v
                return -1 
            s = 0 
            e = len(arr)-1 
            output = -1
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] == v:
                    return arr[mid]
                elif arr[mid] < v:
                    s = mid + 1 
                else: 
                    e = mid - 1
                    output = arr[mid]
            return output 
        
        
        for q in queries: # find the value in the tree
            A = binFindMax(arr, q)
            B = binFindMin(arr, q)
            output.append([A, B])
        
        return output
            
                    
                
                
        
        
        
        

        
        
        
        
