class Solution:
    def hasPath(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> bool:
        visited = set()
        rows = len(maze)
        cols = len(maze[0])
        start = tuple(start)
        destination = tuple(destination)

        def move(pos):
            if pos in visited: return False
            if pos == destination: return True
            visited.add(pos)
            for x in range(4):
                i, j = pos
                if x == 0:
                    while i > 0 and maze[i-1][j] != 1: i -= 1
                if x == 1:
                    while i < rows-1 and maze[i+1][j] != 1: i += 1
                if x == 2:
                    while j > 0 and maze[i][j-1] != 1: j -= 1
                if x == 3:
                    while j < cols-1 and maze[i][j+1] != 1: j += 1
                if move((i, j)):
                    return True

        return move(start)