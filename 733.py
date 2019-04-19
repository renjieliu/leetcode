# def dfs_find(k, graph, output=None):
#     if output ==None:
#         output = []
#     output.append(k)
#     for i in graph[k]:
#         dfs_find(i, graph, output)
#
#     return  output
#
#

def floodFill_dfs(done: 'List[List[int]]', image: 'List[List[int]]', sr: int,  sc: int, newColor: int, originalColor:int):
    if image[sr][sc] == originalColor and done[sr][sc] == None:
        image[sr][sc]= newColor
        done[sr][sc] = 1
        for c in range(sc+1, len(image[0])): #right
            if floodFill_dfs(done,image, sr, c, newColor, originalColor) ==-1:
                break
            # else:
            #     floodFill_dfs(done, image, sr, c, newColor, originalColor)

        for c in range(sc-1,-1,-1): #left
            if floodFill_dfs(done,image, sr, c, newColor, originalColor) ==-1:
                break
            # else:
            #     floodFill_dfs(done, image, sr, c, newColor, originalColor)

        for r in range(sr+1, len(image)): #down
            if floodFill_dfs(done,image, r, sc, newColor, originalColor) ==-1:
                break
            # else:
            #     floodFill_dfs(done, image, r, sc, newColor, originalColor)

        for r in range(sr-1, -1, -1): #up
            if floodFill_dfs(done,image, r, sc, newColor, originalColor) ==-1:
                break
            # else:
            #     floodFill_dfs(done, image, r, sc, newColor, originalColor)

        return image

    else:
        return -1


def floodFill(image: 'List[List[int]]', sr: int, sc: int, newColor: int):
    done = [ [ None for _ in range(len(image[0]))] for _ in range(len(image))]
    return floodFill_dfs( done,image, sr, sc, newColor, image[sr][sc])



print(floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
print(floodFill([[0,0,0],[0,1,1]], sr = 1, sc = 1, newColor = 1))