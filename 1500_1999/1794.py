class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        # to make endFirst-startSecond minimal, is to make endFirst small, and startSecond large
        loc = {}
        for i , c in enumerate(secondString): #find loc of each character in secondString
            if c not in loc:
                loc[c] = []
            loc[c].append(i)

        distance = {}
        for i, c in enumerate(firstString): # just check one letter, and see the diff with curr loc and the last loc in secondString
            if c in loc:
                if i - loc[c][-1] not in distance:
                    distance[i-loc[c][-1]] =0
                distance[i-loc[c][-1]] += 1
        return distance[min(distance.keys())] if distance else 0

