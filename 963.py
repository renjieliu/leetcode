class Solution:
    def minAreaFreeRect(self, points: 'List[List[int]]') -> float:
        def calc_kb(p1, p2):
            if p1[0] == p2[0]:
                return 'invalid'
            else:
                k = (p1[1] - p2[1]) / (p1[0] - p2[0])
                b = p1[1] - k * p1[0]
                return [k, b]

        curve = {}
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                key = (x1, y1, x2, y2)
                center = [(x2 + x1) / 2, (y2 + y1) / 2]
                d2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
                checkExclusion = [i, j]
                curve[key] = [center, d2, checkExclusion]  # curve center,  diameter_Squared, currentPoint
        output = float('inf')
        for k, v in curve.items():
            a = v[0][0]  # center X
            b = v[0][1]  # center Y
            d2 = v[1]  # radius
            checkExclusion = v[2]
            for i in range(len(points)):  # to check if can find a third point on the curve
                if i not in checkExclusion:
                    x1 = points[i][0]
                    y1 = points[i][1]
                    # print( 4*((x1-a) ** 2 + (y1-b) ** 2) ,  d2 )
                    if 4 * ((x1 - a) ** 2 + (
                            y1 - b) ** 2) == d2:  # the point is on the curve, find if the opposite point is also on the curve
                        kb = calc_kb(v[0], points[i])
                        for j in range(len(
                                points)):  # the opposite point need to be on the curve, and on the line from center to current i
                            if j not in checkExclusion and j != i:
                                x2 = points[j][0]
                                y2 = points[j][1]
                                if 4 * ((x2 - a) ** 2 + (y2 - b) ** 2) == d2:
                                    if (kb == 'invalid' and x2 == x1) or kb[0] * x2 + kb[1] == y2:
                                        end1 = points[checkExclusion[0]]
                                        end2 = points[checkExclusion[1]]
                                        w = ((x2 - end1[0]) ** 2 + (y2 - end1[1]) ** 2) ** 0.5
                                        h = ((x2 - end2[0]) ** 2 + (y2 - end2[1]) ** 2) ** 0.5
                                        output = min(output, w * h)

        return output if output != float('inf') else 0








