class Solution:
    def bestHand(self, ranks: 'List[int]', suits: 'List[str]') -> str: # O( N | N )
        r_cnt = defaultdict(lambda:0)
        s_cnt = defaultdict(lambda:0)
        for r in ranks:
            r_cnt[r] +=1
        for s in suits:
            s_cnt[s] += 1
        
        r_mx = max(r_cnt.values()) #max rank value
        
        if len(s_cnt) == 1: # all five cards with same suit
            return "Flush" 
        elif r_mx >= 3: # at least 3 cards of same rank
            return "Three of a Kind"
        elif r_mx >= 2: # at least 2 cars with same rank
            return "Pair" 
        else: # other situation
            return "High Card"



    