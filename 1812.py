class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (coordinates[0] in "bdfh" and int(coordinates[1])%2==1) or (coordinates[0] in "aceg" and int(coordinates[1])%2==0)



