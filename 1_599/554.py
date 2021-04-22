class Solution:
    def leastBricks(self, wall: 'List[List[int]]') -> int:
        hmp = {} # the point there's a break on the wall
        for w in wall:
            s = 0
            for length in w[:-1]:
                s += length
                if s not in hmp:
                    hmp[s] = 0
                hmp[s] += 1

        if len(hmp) == 0: #no break on the wall
            return len(wall)
        else:
            return len(wall) - max(hmp.values()) #length of all the bricks - minus the max(break) on the wall


