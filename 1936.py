class Solution:
    def addRungs(self, rungs: 'List[int]', dist: int) -> int:
        cnt = 0
        rungs.insert(0, 0) #add the 0 to the front, to make the logic easier, as it starts from floor 0
        for i in range(1, len(rungs)):
            spaces = (rungs[i] - rungs[i-1]-1)
            cnt += spaces // dist # how many runes to be inserted between steps
        return cnt
