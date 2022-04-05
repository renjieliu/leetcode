class Solution:
    def findWinners(self, matches: 'List[List[int]]') -> 'List[List[int]]': #O(logN | n)
        win = {}
        loss = {}
        for w, l in matches: # record the winning times and loss times
            if w not in win:
                win[w] = 0 
            win[w] += 1
            if l not in loss:
                loss[l] = 0 
            loss[l] += 1
        
        return [sorted(list(set(win.keys()) - set(loss.keys()))), sorted([k for k, v in loss.items() if v == 1 ])]
    
    
    


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
    
    
    
