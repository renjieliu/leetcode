class Solution:
    def minDistance(self, height: int, width: int, tree: 'List[int]', squirrel: 'List[int]', nuts: 'List[List[int]]') -> int:
        def manDistance(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        nutsDistance_Tree = []
        nutsDistance_Squirrel = []
        for n in nuts:
            nutsDistance_Tree.append(manDistance(n, tree))
            nutsDistance_Squirrel.append(manDistance(n, squirrel))

        output = float('inf')
        total = 2*sum(nutsDistance_Tree) #nut_to_tree_round_trip
        for i in range(len(nutsDistance_Tree)): #pick current, and check the distance to walk.
            output = min( total-nutsDistance_Tree[i] + nutsDistance_Squirrel[i], output  )

        return output



