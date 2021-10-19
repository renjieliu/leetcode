import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def randPoint(self) -> 'List[float]':
        while True:
            x = (self.x_center - self.radius) + 2*self.radius*random.random()
            y = (self.y_center - self.radius) + 2*self.radius*random.random()
            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius**2: #x, y forms a square area, the point need to be within the circle, this is to check if the point is within the circle.
                return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()



