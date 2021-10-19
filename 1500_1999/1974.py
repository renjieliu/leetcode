class Solution:
    def minTimeToType(self, word: str) -> int:
        dist = lambda x, y: min(abs(ord(x) - ord(y)), abs(ord(x) - ord('a')) + abs(ord(y) - ord('z')) + 1, abs(ord(y) - ord('a')) + abs(ord(x) - ord('z')) + 1   ) #clockwise dist and counterclockwise dist (abs dist (x and 'a' + y and 'z') or  (y and 'a' + x and 'z'))
        output = 0
        prev = 'a'
        for c in word:
            output += dist(c,prev) + 1 # move the distance and type
            # print(dist(c, prev), c, prev)
            prev = c
        return output




