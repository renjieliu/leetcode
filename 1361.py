class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: 'List[int]', rightChild: 'List[int]') -> bool:
        def dfs(taken, output, curr, leftChild, rightChild):
            if curr in taken:
                return False
            else:
                taken.append(curr)
                output[-1].append(curr)
                if leftChild[curr] != -1: #check the left Child
                    if dfs(taken, output, leftChild[curr], leftChild, rightChild) == False:
                        return False
                if rightChild[curr] != -1: #check the right Child
                    if dfs(taken, output, rightChild[curr], leftChild, rightChild) == False:
                        return False
                return True

        taken = []
        output = []
        for i in range(n):
            if i not in taken:
                output.append([])
                t = dfs(taken, output, i, leftChild, rightChild)
                if t == False:
                    return False
        if len(output)!=1:
            return False
        return True
