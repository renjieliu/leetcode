class Solution:
    def matchPlayersAndTrainers(self, players: 'List[int]', trainers: 'List[int]') -> int: # O( NlogN | 1 )
        players.sort()
        trainers.sort()  
        cnt = 0 
        p = t = 0 
        while p < len(players) and t < len(trainers): # greedy, check if the trainer can match with the player
            while t < len(trainers) and trainers[t] < players[p]: #keep taking out the trainers unqualified
                t += 1
            if t < len(trainers):
                cnt += 1
                t += 1 
                p += 1
        
        return cnt
    


