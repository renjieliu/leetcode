class Solution:
    def rankTeams(self, votes: 'List[str]') -> str:
        hmp = {}
        for v in votes:
            for i in range(len(v)):
                if v[i] not in hmp:
                    hmp[v[i]] = [0]*len(v) #create a scorecard for each letter
                hmp[v[i]][i]+=1
        rank = []
        for k, v in hmp.items():
            rank.append(v+[k])
        rank.sort(key = lambda x:x[-1]) #sort by the letter first to save the alphabetical order
        rank.sort(key = lambda x:x[:-1], reverse = True ) #sort by the actual ranking descendingly.
        output = ""
        for r in rank:
            output+=str(r[-1])
        return output
        
                
                