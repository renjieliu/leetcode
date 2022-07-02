class Solution:
    def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]': #O(N**2 | N)
        people.sort(key = lambda x: x[0])
        output = [[float('inf'), float('inf')] for p in people] 
        for h, c in people: #go through the people
            cnt = 0  #how many people in the front are >= current 
            for i in range(len(output)): # as long as there's an empty slot, just put people there
                if cnt == c and output[i][0] == float('inf'):
                    output[i][0] = h
                    output[i][1] = c 
                    break 
                cnt += 1 if output[i][0] >= h else 0
        return output
                    


# previous solution

# class Solution:
#     def reconstructQueue(self, people: 'List[List[int]]') -> 'List[List[int]]':
#         people.sort(key = lambda x : x[0])
#         output = [ [float('inf'),float('inf')] for _ in range(len(people)) ]
#         #print(people)
#         for height, c in people:
#             cnt = 0
#             for i in range(len(output)):
#                 if c == cnt and output[i][0] == float('inf'): #as long as a free slot, just to put it there
#                     output[i] = [height, c]
#                     break
#                 elif output[i][0] >= height:
#                     cnt += 1
#                 #print(height,c , output )
#         return output


