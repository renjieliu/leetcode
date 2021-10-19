class Solution:
    def minAreaRect(self, points: 'List[List[int]]') -> int:
        dict_p = {}
        points.sort()
        for p in points:
            key = tuple(p)
            dict_p[key] = 1
        output = float('inf')
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                if abs(x2 - x1) > output:
                    break
                elif x1 != x2 and y1 != y2:
                    key_1 = (x1, y2)  # str(x1) + '-' + str(y2)
                    key_2 = (x2, y1)  # str(x2) + '-' + str(y1)
                    if key_1 not in dict_p or key_2 not in dict_p:
                        continue
                    else:
                        output = min(output, abs(x2 - x1) * abs(y2 - y1))
        return output if output != float('inf') else 0

