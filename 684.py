class Solution:
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        trees = [edges[0]] #initialize the tree
        i = 1
        while i < len(edges): #go through the edge list
            #print(trees)
            find = []
            j = 0
            while j < len(trees): # check if match with any current tree
                t = trees[j]
                #print('t - ', t)
                if edges[i][0] in t and edges[i][1] in t: #redudant connection. both nodes are in current tree
                    return edges[i]
                elif edges[i][0] in t or edges[i][1] in t: #add to the tree
                    t+=edges[i]
                    find.append(j)
                j+=1
            if find == []: #new node, cannot find any match
                trees.append(edges[i])
            elif len(find) == 2: # current one is the bridge, need to merge both trees
                trees[find[0]]+=trees[find[1]]
                trees = trees[:find[1]] + trees[find[1]+1:]
            i+=1