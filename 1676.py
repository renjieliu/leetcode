# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def flat(arr, node, curr, hmp):
            if node.val in hmp:
                arr.append(curr + [node.val])
            else:
                if node.left:
                    flat(arr, node.left, curr + [node.val], hmp)
                if node.right:
                    flat(arr, node.right, curr + [node.val], hmp)

        def sameHead(arr):
            output = arr[0][0]  # set the first value as the output
            head = []
            while arr:
                if arr[0]:
                    curr = arr[0][0]
                    comp = set()
                    cnt = 0
                    for a in arr:
                        if a:
                            comp.add(a.pop(0))
                            cnt += 1
                    if len(comp) == 1 and cnt == len(arr):  # all the values are same in all the arr
                        head.append(curr)
                    else:
                        break
                else:
                    break
            return head[-1]

        def findLCA(output, target, node):
            if node.val == target:
                output.append(node)
            else:
                if node.left:
                    findLCA(output, target, node.left)
                if node.right:
                    findLCA(output, target, node.right)

        arr = []
        hmp = {n.val for n in nodes}
        flat(arr, root, [], hmp)

        # print(arr)

        target = sameHead(arr)
        output = []
        findLCA(output, target, root)
        return output[0]























