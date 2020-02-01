class Solution:
    def findLonelyPixel(self, picture: 'List[List[str]]') -> int:
        c_cnt = [] #this is used to store the count of 'B' for each column
        for c in range(len(picture[0])):
            curr = 0
            for r in range(len(picture)):
                if picture[r][c] == 'B':
                    curr+=1
            c_cnt.append(curr)
        output = 0
        for r in range(len(picture)): # foreach line, if only one 'B', look up in c_cnt, to see how many B in that column
            curr = []
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    curr.append(c)
            if len(curr) ==1 and c_cnt[curr[-1]] ==1:
                output +=1
        return output