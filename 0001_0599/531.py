class Solution:
    def findLonelyPixel(self, picture: 'List[List[str]]') -> int: # O( MN | MN )
        r_cnt = defaultdict(lambda: 0)
        c_cnt = defaultdict(lambda: 0)
        B = set()
        for r in range(len(picture)): # find all the "Black" in the picture
            for c in range(len(picture[r])):
                if picture[r][c] == "B":
                    r_cnt[r] += 1 
                    c_cnt[c] += 1 
                    B.add((r, c))
        return sum(1 for r, c in B if r_cnt[r] == c_cnt[c] == 1) # for the founded black pixels, no other black pixels in the same col and row
    


# previous solution

# class Solution:
#     def findLonelyPixel(self, picture: 'List[List[str]]') -> int:
#         c_cnt = [] #this is used to store the count of 'B' for each column
#         for c in range(len(picture[0])):
#             curr = 0
#             for r in range(len(picture)):
#                 if picture[r][c] == 'B':
#                     curr+=1
#             c_cnt.append(curr)
#         output = 0
#         for r in range(len(picture)): # foreach line, if only one 'B', look up in c_cnt, to see how many B in that column
#             curr = []
#             for c in range(len(picture[0])):
#                 if picture[r][c] == 'B':
#                     curr.append(c)
#             if len(curr) ==1 and c_cnt[curr[-1]] ==1:
#                 output +=1
#         return output



