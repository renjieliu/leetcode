# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y or sea.hasShips(topRight, bottomLeft)==False:
            return 0
        elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return sea.hasShips(topRight, bottomLeft)
        else:#split into 4 part, and avoid double counting on the border.
            mid_x = (topRight.x + bottomLeft.x)//2
            mid_y = (topRight.y + bottomLeft.y)//2
            A = self.countShips(sea, topRight, Point(mid_x+1,mid_y+1)) #top right
            B = self.countShips(sea, Point(mid_x,mid_y), bottomLeft) #low left
            C = self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x,mid_y+1)) #top left
            D = self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x+1, bottomLeft.y)) # low right
            return A+B+C+D
            
        
        


# previous approach

# # """
# # This is Sea's API interface.
# # You should not implement it, or speculate about its implementation
# # """
# #class Sea(object):
# #    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
# #
# #class Point(object):
# #	def __init__(self, x: int, y: int):
# #		self.x = x
# #		self.y = y

# class Solution(object):
#     def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
#         if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y or sea.hasShips(topRight, bottomLeft) == False: # check if current region is valid and it has ships.
#             return 0

#         if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
#             return sea.hasShips(topRight, bottomLeft)

#         mid_x = (bottomLeft.x + topRight.x)//2
#         mid_y = (bottomLeft.y + topRight.y)//2

#         #divide into 4 regions, and avoid double counting on the border
#         A = self.countShips(sea, Point(mid_x, mid_y), bottomLeft) #left bottom area
#         B = self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x+1, bottomLeft.y)) #right bottom area
#         C = self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y+1)) #left upper area
#         D = self.countShips(sea, topRight, Point(mid_x+1, mid_y+1)) # right upper area

#         return A + B + C + D


    

    