class Solution:
    def minAvailableDuration(self, slots1: 'List[List[int]]', slots2: 'List[List[int]]', duration: int) -> 'List[int]': #O(NlogN | 1)
        slots1.sort(); slots2.sort()
        while slots1 and slots2:
            a, b = slots1[0]
            c, d = slots2[0]
            if c <= a <= d or a <= c <= b : # overlapping
                if min(b, d) - max(a, c) >= duration:
                    return [max(a, c) , max(a, c) + duration]
            if b <= d: #pop the one ends first
                slots1.pop(0)
            else:
                slots2.pop(0)
            
        return []




# previous solution

# class Solution:
#     def minAvailableDuration(self, slots1: 'List[List[int]]', slots2: 'List[List[int]]', duration: int) -> 'List[int]':
#         slots1.sort(key = lambda x:x[0])
#         slots2.sort(key = lambda x:x[0])
#         overlapping_length = lambda a, b: 0 if a[1]<b[0] or b[1]<a[0] else min(a[1],b[1]) - max(a[0],b[0])
#         while slots1 and slots2:
#             #print(overlapping_length(slots1[0], slots2[0]))
#             if overlapping_length(slots1[0], slots2[0])>=duration:
#                 return [max(slots1[0][0],slots2[0][0]), max(slots1[0][0],slots2[0][0])+duration]
#             else:
#                 if slots1[0][1] <= slots2[0][1]: #take out the one ends first
#                     slots1.pop(0)
#                 else:
#                     slots2.pop(0)
#         return []


# previous approach
# class Solution:
#     def minAvailableDuration(self, slots1: 'List[List[int]]', slots2: 'List[List[int]]', duration: int):
#         slots1.sort()
#         slots2.sort()
#         i = j = 0
#         while i < len(slots1):
#             while j < len(slots2):  # find overlapping
#                 if slots1[i][0] > slots2[j][1]:  # to increase j
#                     j += 1
#                 elif slots2[j][0] > slots1[i][1]:  # to increase i
#                     break
#                 elif slots1[i][0] <= slots2[j][0] <= slots1[i][1] and slots1[i][0] <= slots2[j][1] <= slots1[i][
#                     1]:  # s2 within s1
#                     if slots2[j][1] - slots2[j][0] >= duration:
#                         return [slots2[j][0], slots2[j][0] + duration]
#                     else:
#                         break
#                 elif slots2[j][0] <= slots1[i][0] <= slots2[j][1] and slots2[j][0] <= slots1[i][1] <= slots2[j][
#                     1]:  # s1 within s2
#                     if slots1[i][1] - slots1[i][0] >= duration:
#                         return [slots1[i][0], slots1[i][0] + duration]
#                     else:
#                         break
#                 elif slots1[i][0] <= slots2[j][0] <= slots1[i][1]:  # partial overlapping
#                     if slots1[i][1] - slots2[j][0] >= duration:
#                         return [slots2[j][0], slots2[j][0] + duration]
#                     else:
#                         break
#                 elif slots2[j][0] <= slots1[i][0] <= slots2[j][1]:  # partial overlapping
#                     if slots2[j][1] - slots1[i][0] >= duration:
#                         return [slots1[i][0], slots1[i][0] + duration]
#                     else:
#                         break
#
#             i += 1
#
#         return []
#
#
