class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = {(0,0)}
        curr = [0,0]
        for p in path:
            #print(point, curr)
            if p == 'N':
                curr[1]+=1
                if (curr[0], curr[1]) not in point:
                    point.add((curr[0], curr[1]))
                else:
                    return True
            elif p == 'S':
                curr[1]-=1
                if (curr[0], curr[1]) not in point:
                    point.add((curr[0], curr[1]))
                else:
                    return True
            elif p == 'W':
                curr[0]-=1
                if (curr[0], curr[1]) not in point:
                    point.add((curr[0], curr[1]))
                else:
                    return True
            elif p == 'E':
                curr[0]+=1
                if (curr[0], curr[1]) not in point:
                    point.add((curr[0], curr[1]))
                else:
                    return True
        return False
