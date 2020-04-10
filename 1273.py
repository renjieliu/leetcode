class Solution:
    def deleteTreeNodes(self, nodes: int, parent: 'List[int]', value: 'List[int]') -> int:
        kid = {}
        for i, c in enumerate(parent): #find the kids array for the current index
            if c not in kid:
                kid[c] = []
            kid[c].append(i)
        output = [nodes]

        def sumKid(kid, key, value, output):
            currPath = [value[key]]
            for c in kid[key]:
                if c in kid:
                    currPath += sumKid(kid, c, value, output)
                else:
                    if value[c] == 0: #the leaf itself is 0 , no need to add to the path
                        output[0] -= 1
                    else:
                        currPath.append(value[c])
            del kid[key]

            if sum(currPath) == 0:
                output[0] -= (len(currPath))
                currPath = []
            #print(currPath)
            return currPath

        rootPos = kid[-1][0] #-1 will only have one kid, the root
        rootVal = value[rootPos]
        total = sumKid(kid, -1, value, output)
        if total == 0:
            return 0
        else:
            for v in kid.values():  #it has not been iterated, it means it does not belong to the tree starting at 0
                output[0]-=len(v)
            return output[0]