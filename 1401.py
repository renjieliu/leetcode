class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def distance(A, B):
            return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

        circle_up = [x_center, y_center + radius]
        circle_down = [x_center, y_center - radius]
        circle_left = [x_center - radius, y_center]
        circle_right = [x_center + radius, y_center]
        circle_center = [x_center, y_center]
        square_upperLeft = [x1, y2]
        square_bottomLeft = [x1, y1]
        square_upperRight = [x2, y2]
        square_bottomRight = [x2, y1]
        # print(circle_up, x1, x2, y1,y2)
        # print(circle_down, x1, x2, y1,y2)
        # print(circle_left, x1, x2, y1,y2)
        # print(circle_right, x1, x2, y1,y2)

        if (distance(square_upperLeft, circle_center) ** 2 <= radius ** 2  # square point within circle
                or distance(square_bottomLeft, circle_center) ** 2 <= radius ** 2
                or distance(square_upperRight, circle_center) ** 2 <= radius ** 2
                or distance(square_bottomRight, circle_center) ** 2 <= radius ** 2
                or (y1 <= circle_down[1] <= y2 and x1 <= circle_down[0] <= x2)  # circle has part in the square
                or (y1 <= circle_up[1] <= y2 and x1 <= circle_up[0] <= x2)
                or (y1 <= circle_right[1] <= y2 and x1 <= circle_right[0] <= x2)
                or (y1 <= circle_left[1] <= y2 and x1 <= circle_left[0] <= x2)
                # square across the circle, both egdes are within the circle, but 4 points are not
                or (circle_left[0] <= x1 <= circle_right[0] and circle_left[0] <= x2 <= circle_right[0] and y2 >=
                    circle_up[1] and y1 <= circle_down[1])
                or (circle_down[1] <= y1 <= circle_up[1] and circle_down[1] <= y2 <= circle_up[1] and x2 >=
                    circle_right[0] and x1 <= circle_left[0])
        ):
            return True
        return False