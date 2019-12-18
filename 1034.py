class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(check, sr, sc, grid, original_color):
            if sr==len(grid) or sc==len(grid[0]) or check[sr][sc] == 'c' or grid[sr][sc] != original_color:
                return -1 
            else:
                check[sr][sc] = 'c'#to mark it's a candidate to change color 
                r = sr+1 #look down             
                while r < len(grid):
                    if dfs(check, r, sc, grid, original_color) ==-1 :
                        break
                    r+=1
                r = sr-1 #look up
                while r > -1:
                    if dfs(check, r,sc, grid, original_color) ==-1:
                        break
                    r-=1
                c=sc-1 #look left
                while c>-1:
                    if dfs(check,sr,c, grid, original_color) ==-1:
                        break
                    c-=1
                c=sc+1
                while c<len(grid[0]):
                    if dfs(check, sr, c, grid, original_color) ==-1:
                        break
                    c+=1
        #using DFS to mark all the connected square as "c", and reverse the ones not on the border              
        check = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] 
        original_color = grid[r0][c0]
        dfs(check, r0, c0, grid, original_color)
        #print(check)
        output =[]
        for r in range(len(grid)):
            output.append([])
            for c in range(len(grid[0])):
                if check[r][c] == 0:
                    output[-1].append(grid[r][c])
                else:
                    if r==0 or c==0 or r == len(grid)-1 or c == len(grid[0])-1:
                        output[-1].append(color)
                    else:
                        if check[r-1][c] == "c" and check[r+1][c] == "c" and check[r][c-1] =="c" and check[r][c+1] =="c":
                            output[-1].append(grid[r][c])
                        else:
                            output[-1].append(color)
        return output
                        
                        
                        
                        
                        
                        
            
        