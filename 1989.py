class Solution:
    def catchMaximumAmountofPeople(self, team: 'List[int]', dist: int) -> int:
        zeroLoc = 0
        cnt = 0
        for i in range(len(team)):
            if team[i] == 1:
                while zeroLoc < max(0, i - dist): #make the zeroLoc in the range
                    zeroLoc += 1
                while zeroLoc <= min(i + dist, len(team)-1) and team[zeroLoc] == 1: #make the zeroLoc in the range
                    zeroLoc += 1
                if zeroLoc <= len(team)-1 and team[zeroLoc] == 0:
                    #print(i, zeroLoc)
                    zeroLoc += 1
                    cnt += 1
        return cnt

