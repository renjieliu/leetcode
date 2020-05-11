class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: int, sc: int, newColor: int) -> 'List[List[int]]':
        def fill(check, image, sr, sc, newColor, target):
            image[sr][sc] = newColor
            check[sr][sc] = 1
            if sr-1 >-1 and image[sr-1][sc] == target and check[sr-1][sc] == 0:
                fill(check, image, sr-1, sc, newColor, target)
            if sr+1<len(image) and image[sr+1][sc] == target  and check[sr+1][sc] == 0:
                fill(check, image, sr+1, sc, newColor, target)
            if sc-1>-1 and image[sr][sc-1] == target  and check[sr][sc-1] == 0 :
                fill(check, image, sr, sc-1, newColor, target)
            if sc+1 < len(image[0]) and image[sr][sc+1] == target and check[sr][sc+1] ==0:
                fill(check, image, sr, sc+1, newColor, target)
        check = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        fill(check, image, sr, sc, newColor, image[sr][sc])
        return image