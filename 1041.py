class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # up, right, down, left
        x = y = 0
        face = 0  # face north
        for i in instructions:
            if i == "L":
                face = (face + 3) % 4
            elif i == "R":
                face = (face + 1) % 4
            else:
                x += direction[face][0]
                y += direction[face][1]
        if x == y == 0 or face != 0:  # if it can return to the starting point, or it's not facing north
            return True
        return False







