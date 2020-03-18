# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode,
                   target: int) -> bool:  # flatten and using binary search: O(nlogn)
        def bin(arr, t):
            s = 0
            e = len(arr) - 1
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] == t:
                    return mid
                elif arr[mid] > t:
                    e = mid - 1
                elif arr[mid] < t:
                    s = mid + 1
            return -1

        def flat(node, lst):
            if node.left == node.right == None:
                lst.append(node.val)
            else:
                lst.append(node.val)
                if node.left != None:
                    flat(node.left, lst)
                if node.right != None:
                    flat(node.right, lst)

        lst1 = []
        lst2 = []
        if root1 != None:
            flat(root1, lst1)
        if root2 != None:
            flat(root2, lst2)
        lst2.sort()
        for l in lst1:
            if bin(lst2, target - l) != -1:
                return True
        return False


