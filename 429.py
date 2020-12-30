
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if root == None: return []
        output = []
        layers = [[root]]
        while layers:  # using BFS to traverse
            currLayer = layers.pop(0)
            output.append([])
            for node in currLayer:
                output[-1].append(node.val)
                for c in node.children:  # it has children and need to be added to the next layer
                    if layers == []:
                        layers.append([])
                    layers[-1].append(c)

        return output




