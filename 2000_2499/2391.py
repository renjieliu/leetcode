class Solution:
    def garbageCollection(self, garbage: 'List[str]', travel: 'List[int]') -> int: # O( N | N )
        pre_travel = [0, 0] # accumulate for the travel time, [0, 0], first 0 is to make the dp[-1] easier, the 2nd is time need to reach the first stop, which is 0
        for t in travel:
            pre_travel.append(pre_travel[-1] + t)
        M_total = 0
        P_total = 0
        G_total = 0 
        M_last = 0
        P_last = 0
        G_last = 0
        for i, g in enumerate(garbage): # count how many each type of garbage is there, and where is the last location 
            M_total += g.count('M')
            P_total += g.count('P')
            G_total += g.count('G')
            if g.count('M'):
                M_last = i+1 # this will be index in the pre_travel , hence + 1
            if g.count('P'):
                P_last = i+1
            if g.count('G'):
                G_last = i+1
        
        return M_total + pre_travel[M_last] + P_total + pre_travel[P_last] + G_total + pre_travel[G_last]
        

        
