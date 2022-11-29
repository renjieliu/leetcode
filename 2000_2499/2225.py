class Solution:
    def findWinners(self, matches: 'List[List[int]]') -> 'List[List[int]]': # O( NlogN | N )
        players = set() # record all the players
        loser = defaultdict(lambda: 0) # count how many times the player lost
        for w, l in matches:
            players.add(w)
            players.add(l)
            loser[l] += 1 
        
        winner = sorted(list(players - set(loser.keys()))) # all the players - losers
        lose_1_time = sorted([k for k, v in loser.items() if v == 1])  #if the player lost only one time
        return [winner, lose_1_time]
                
        

    



# previous solution

# class Solution:
#     def findWinners(self, matches: 'List[List[int]]') -> 'List[List[int]]': #O(logN | n)
#         win = {}
#         loss = {}
#         for w, l in matches: # record the winning times and loss times
#             if w not in win:
#                 win[w] = 0 
#             win[w] += 1
#             if l not in loss:
#                 loss[l] = 0 
#             loss[l] += 1
        
#         return [sorted(list(set(win.keys()) - set(loss.keys()))), sorted([k for k, v in loss.items() if v == 1 ])]
    
    
    


# previous solution

# class Solution:
#     def findWinners(self, matches: 'List[List[int]]') -> 'List[List[int]]': #O(logN | n)
#         win = {}
#         loss = {}
#         for w, l in matches: # record the winning times and loss times
#             if w not in win:
#                 win[w] = 0 
#             win[w] += 1
#             if l not in loss:
#                 loss[l] = 0 
#             loss[l] += 1
        
#         return [sorted(list(set(win.keys()) - set(loss.keys()))), sorted([k for k, v in loss.items() if v == 1 ])]
    
    
    
