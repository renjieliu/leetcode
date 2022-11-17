# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: 'Optional[TreeNode]') -> int: # O( NlogN | N )
        def flat(hmp, lvl, node): # put all the nodes on the same level together
            if node:
                hmp[lvl].append(node.val) 
                flat(hmp, lvl+1, node.left)
                flat(hmp, lvl+1, node.right)
        
        def swapCnt(arr): #count the swaps to be made to make arr sorted
            loc = {} # record the location of each number
            for i , n in enumerate(arr):
                loc[n] = i
            lookup = sorted(arr) 
            i = 0 
            n = len(arr)
            cnt = 0
            while i < n: # simulation to place the number to the right place
                currN = arr[i] # current number
                lkpN = lookup[i] # looked up number
                loc_currN = loc[currN] # the location of current number
                loc_lkpN = loc[lkpN] # the location of the looked number
                
                if currN != lkpN:
                    arr[i], arr[loc_lkpN] = arr[loc_lkpN], arr[i] # swap the 2 numbers
                    loc[currN] = loc_lkpN  # need to update the location hashmap
                    loc[lkpN] = currN
                    cnt += 1  
                i += 1
                #print(arr)
            
            return cnt 
        
        
        hmp = defaultdict(lambda: [])
        flat(hmp, 1, root) 
        #print(hmp)
        cnt = 0 
        for k, nums in hmp.items():
            cnt += swapCnt(nums)
        return cnt


        
