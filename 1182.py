class Solution:
    def shortestDistanceColor(self, colors: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        hmp_left = {1: float('inf'), 2: float('inf'), 3: float('inf')}  # closet color on the left
        hmp_right = {1: float('inf'), 2: float('inf'), 3: float('inf')}  # closet color on the right
        dp_left, dp_right = [[] for _ in range(len(colors))], [[] for _ in range(len(colors))]
        for i in range(len(colors)):
            hmp_left[colors[i]] = i
            dp_left[i] = [hmp_left[1], hmp_left[2], hmp_left[3]]
        for i in range(len(colors) - 1, -1, -1):
            hmp_right[colors[i]] = i
            dp_right[i] = [hmp_right[1], hmp_right[2], hmp_right[3]]
        output = []
        # print(dp_left, dp_right)
        for q in queries:
            pos = q[0]
            color = q[1] - 1  # the position in the dp_left/dp_right,color 1 at pos 0 in the dp
            if dp_left[pos][color] == float('inf'):
                if dp_right[pos][color] != float('inf'):
                    output.append(abs(dp_right[pos][color] - pos))
                else:  # the number cannot be found
                    output.append(-1)
            else:
                if dp_right[pos][color] == float('inf'):
                    output.append(abs(dp_left[pos][color] - pos))
                else:
                    output.append(min(abs(dp_right[pos][color] - pos), abs(dp_left[pos][color] - pos)))
        return output


