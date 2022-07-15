class Solution:
    def shortestDistanceColor(self, colors: 'List[int]', queries: 'List[List[int]]') -> 'List[int]': # O( NlogN | N )
        hmp = defaultdict(lambda: [])
        for i, c in enumerate(colors):
            hmp[c].append(i)
            
        def binFind(arr, v): # to find the where should v belong, if to insert it to the array
            if v > arr[-1]:
                return v - arr[-1]
            elif v < arr[0]:
                return arr[0] - v
            else:
                s = 0 
                e = len(arr)-1
                while s <= e:
                    mid = s - (s-e)//2
                    if arr[mid] == v:
                        return 0 
                    elif arr[mid] > v:
                        e = mid - 1 
                    else:
                        s = mid + 1
                
                return min(abs(arr[s-1]-v), abs(arr[s]-v)) #it's either the previous one, or current one.
        
        output = []
        for i, c in queries:
            if c not in hmp:
                output.append(-1)
            else:
                output.append(binFind(hmp[c], i))
        return output    
    
    
    
# previous solution

# class Solution:
#     def shortestDistanceColor(self, colors: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
#         hmp = defaultdict(lambda: [])
#         for i , c in enumerate(colors):
#             hmp[c].append(i)
#         def binFind(arr, v): #to find the last number smaller than v
#             s = 0
#             e = len(arr)-1
#             output = 0
#             while s<=e:
#                 mid = s-(s-e)//2
#                 if arr[mid] > v:
#                     e = mid -1
#                 elif arr[mid] <= v:
#                     output = mid
#                     s = mid + 1
#             return output

#         output = []
#         for pos, color in queries:
#             if color not in hmp:
#                 output.append(-1)

#             elif colors[pos] == color:
#                 output.append(0)

#             else:
#                 loc = binFind(hmp[color], pos)
#                 if loc == len(hmp[color])-1:
#                     dist = abs(hmp[color][-1]-pos)
#                 else:
#                     dist = min(abs(hmp[color][loc]-pos), abs(hmp[color][loc+1]-pos))
#                 output.append(dist)
#         return output




# previous approach
# class Solution:
#     def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
#         hmp_left={1: float('inf'), 2:float('inf'), 3:float('inf')} #closet color on the left
#         hmp_right={1:float('inf'), 2:float('inf'), 3:float('inf')} #closet color on the right
#         dp_left, dp_right = [[] for _ in range(len(colors))],  [[] for _ in range(len(colors))]
#         for i in range(len(colors)):
#             hmp_left[colors[i]] = i
#             dp_left[i] =  [hmp_left[1], hmp_left[2], hmp_left[3]]
#         for i in range(len(colors)-1,-1,-1):
#             hmp_right[colors[i]] = i
#             dp_right[i] = [hmp_right[1], hmp_right[2], hmp_right[3]]
#         output = []
#         #print(dp_left, dp_right)
#         for q in queries:
#             pos = q[0]
#             color = q[1]-1 #the position in the dp_left/dp_right,color 1 at pos 0 in the dp
#             if dp_left[pos][color] == float('inf'):
#                 if dp_right[pos][color] != float('inf'):
#                     output.append(abs(dp_right[pos][color] - pos ))
#                 else: #the number cannot be found
#                     output.append(-1)
#             else:
#                 if dp_right[pos][color] == float('inf'):
#                     output.append(abs(dp_left[pos][color] - pos ))
#                 else:
#                     output.append( min(abs(dp_right[pos][color] - pos ),abs(dp_left[pos][color] - pos )))
#         return output

