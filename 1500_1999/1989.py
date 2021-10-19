class Solution:
    def catchMaximumAmountofPeople(self, team: 'List[int]', dist: int) -> int:
        p0 = p1 = 0 # pointer for 1 and 0
        cnt = 0
        while p1 < len(team): # move the pointer for 0
            if team[p1] == 1:
                while p0 < len(team) and p0 <= p1+dist: # move the pointer for 0
                    if team[p0] == 0 and p1-dist <= p0 <= p1+dist:
                        cnt += 1
                        p0 += 1 #advance the 0 pointer after count
                        break
                    p0+=1
            p1+=1
        return cnt

