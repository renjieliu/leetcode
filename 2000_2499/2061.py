class Solution:
    def numberOfCleanRooms(self, room: 'List[List[int]]') -> int:
        direction = [[0,1], [1,0], [0,-1], [-1,0]]  #right, down, left, up
        r = c = d = 0
        seen = {(r,c,d)} #(r,c, nxtdirection)
        cleaned = {(r,c)}
        while True:
            if -1 < r+direction[d][0] < len(room) and -1 < c+direction[d][1] < len(room[0]): #not on the border
                if room[r+direction[d][0]][c+direction[d][1]] == 1:
                    d = (d+1)%len(direction)
                else:
                    seen.add((r, c, d))
                    cleaned.add((r,c))
                    r+=direction[d][0] 
                    c+=direction[d][1] 
                    
            else:
                d = (d+1)%len(direction)
            
            if (r, c, d) in seen:
                return len(cleaned)
            
