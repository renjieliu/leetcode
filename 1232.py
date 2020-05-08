class Solution:
    def checkStraightLine(self, coordinates: 'List[List[int]]') -> bool:
        if len(coordinates) == 2: return True
        else:
            x = coordinates[0][0]-coordinates[1][0]
            y = coordinates[0][1] - coordinates[1][1]
            k = 0 if x ==0 else y/x
            b = coordinates[0][1] if k == 0 else coordinates[0][1] - k*coordinates[0][0]
            for c in coordinates :
                if c[1] != k*c[0] + b:
                    return False
            return True