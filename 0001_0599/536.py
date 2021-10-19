# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode: #"4(2(3)(1))(6(5))"
        curr = ""
        for i, c in enumerate(s):
            if c != "(":
                curr+=c
            else:
                s = s[i:]
                break
        if curr == "": return None
        root=TreeNode(int(curr))
        left = 1
        end = None
        for i in range(1, len(s)): #find the pair loc of (, and substring as leftStr. the rest will be rightStr
            if s[i]=="(":
                left +=1
            elif s[i] == ")":
                left -= 1
                if left == 0:
                    end = i
                    break
        if end != None:
            root.left = self.str2tree(s[1:end])
            root.right = self.str2tree(s[end+2:-1])

        return root