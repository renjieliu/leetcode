class Solution:
    def removeCoveredIntervals(self, intervals: 'List[List[int]]') -> int: #O(NlogN) approach
        intervals.sort(key = lambda x: x[1])
        intervals.sort(key = lambda x: x[0]) 
        s = intervals[0][0]
        e = intervals[0][1]
        rmv = 0
        for i in range(1, len(intervals)):
            if s <= intervals[i][0] <= intervals[i][1] <= e: # previous range can cover current intervals, no need to set the new s and e, as we will be using the previous s, e for the next one
                rmv+=1 
            elif intervals[i][0]<= s<=e<=intervals[i][1]:#current can cover previous
                rmv+=1
                s, e = intervals[i]  #turn the current interval to the new s and e
            else:
                s, e = intervals[i]  #turn the current interval to the new s and e
        
        return len(intervals)-rmv #total length - the one to be removed
    

# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int: #O(N2) approach 
#         def cover(a, b): #to check if b covers a 
#             return b[0] <= a[0] and b[1] >= a[1] and a!=b
        
#         cnt = 0
#         for i in range(len(intervals)): #for each one in the intervals, to check there's another one to cover it
#             for j in range(len(intervals)):
#                 if cover(intervals[i], intervals[j]):
#                     cnt +=1 
#                     break
#         return len(intervals) - cnt 







# previous approach

# class Solution:
#     def removeCoveredIntervals(self, intervals: 'List[List[int]]') -> int:
#         intervals.sort(key = lambda x:x[1], reverse = True ) #same start, put the larger end at first
#         intervals = sorted(intervals,key = lambda x: x[0])
#         # print(intervals)
#         curr = [intervals[0][0], intervals[0][1]]
#         cnt = 0 #the count of removed intervals
#         for s, e in intervals[1:]:
#             if curr[0]<=e<=curr[1]:
#                 cnt+=1
#             else:
#                 curr[1] = e
#             #print(curr, cnt)
#         return len(intervals) - cnt

# previous approach
# class Solution:
#     def removeCoveredIntervals(self, intervals: 'List[List[int]]') -> int:
#         def dfs(check, start, cnt, rng, intervals):
#             if check[start] != 0:  # it has been checked before
#                 return -1
#             else:
#                 check[start] = cnt
#                 curr = start + 1
#                 while curr < len(intervals):
#                     A = rng
#                     B = intervals[curr]
#                     if intervals[curr][0] > rng[1]:
#                         return 0
#                     elif (B[0] <= A[0] <= A[1] <= B[1]) or (
#                             A[0] <= B[0] <= B[1] <= A[1]):  # B within A or A within B
#                         a = intervals[curr][1] - intervals[curr][0]
#                         b = rng[1] - rng[0]
#                         currRng = intervals[curr] if a > b else rng  # to get the larger range for checking
#                         if dfs(check, curr, cnt, currRng, intervals) == 0:
#                             break
#                     curr += 1
#
#                 return 0
#
#         intervals.sort()
#         check = [0] * len(intervals)
#         cnt = 0
#         for i in range(len(intervals)):
#             if check[i] == 0:
#                 cnt += 1
#                 rng = intervals[i]  # the range to check
#                 dfs(check, i, cnt, rng, intervals)
#         return cnt