class Solution:
    def findBlackPixel(self, picture: 'List[List[str]]', N: int) -> int:
        keys = ['-'.join(r) for r in picture]  # make each row into a string.
        goodrow = set()  # these rows could be a good candidate
        for r in range(len(picture)):
            cnt = 0
            for c in picture[r]:
                cnt += 1 if c == 'B' else 0
            if cnt == N:
                goodrow.add(r)
        hmp = {}
        for r in goodrow:
            if keys[r] not in hmp:
                hmp[keys[r]] = []
            hmp[keys[r]].append(r)

        goodcol = set()
        for c in range(len(picture[0])):
            cnt = 0
            for r in range(len(picture)):
                if picture[r][c] == 'B':
                    cnt += 1
            if cnt == N:
                goodcol.add(c)

        output = 0
        for r in goodrow:
            for c in goodcol:
                if picture[r][c] == 'B' and len(hmp[keys[r]]) >= N:
                    output += 1
        return output


















