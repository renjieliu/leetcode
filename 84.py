class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> int:
        if heights == []:  return 0
        pos = [0]  # mono increasing stk. keep popping if current number is smaller than than the prev one.
        output = 0
        r = 1
        while r < len(heights):
            curr = heights[r]
            while pos and heights[pos[-1]] >= curr:
                P = pos.pop()  # previous max position
                W = r if pos == [] else r - (pos[-1] + 1)
                H = heights[P]
                output = max(output, W * H)
            pos.append(r)
            r += 1

        while pos:
            P = pos.pop()
            W = r if pos == [] else r - (pos[-1] + 1)
            H = heights[P]
            output = max(output, W * H)
        return output

