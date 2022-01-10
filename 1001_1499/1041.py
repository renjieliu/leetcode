class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]] #up, right, down, left
        d = 0 # initial was facing up
        x = y = 0
        for i in instructions:
            if i == "G":
                x += direct[d][0]
                y += direct[d][1]
            elif i == "R":
                d+=1
            elif i == "L":
                d-=1
            d %= len(direct)
        
        return x==y==0 or d!=0 # if back to the orginal point after one iteration or not facing up, it will go back.
    
    


# previous approach
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # up, right, down, left
#         x = y = 0
#         face = 0  # face north
#         for i in instructions:
#             if i == "L":
#                 face = (face + 3) % 4
#             elif i == "R":
#                 face = (face + 1) % 4
#             else:
#                 x += direction[face][0]
#                 y += direction[face][1]
#         if x == y == 0 or face != 0:  # if it can return to the starting point, or it's not facing north
#             return True
#         return False







