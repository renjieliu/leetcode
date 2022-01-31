class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> int:
        if heights == []:  return 0
        pos = [0] #mono increasing stk. keep popping if current number is smaller than than the prev one.
        output = 0
        r = 1
        while r < len(heights):
            curr = heights[r]
            while pos and heights[pos[-1]] > curr:
                P = pos.pop() #previous max position
                W = r if pos == [] else r-(pos[-1]+1)
                H = heights[P]
                output = max(output, W*H)
            pos.append(r)
            r+=1

        while pos:
            P = pos.pop()
            W = r if pos ==[] else r-(pos[-1]+1)
            H = heights[P]
            output = max(output, W*H)
        return output
    
# previous approach

# class Solution:
#     def largestRectangleArea(self, heights: 'List[int]') -> int:
#         if heights == []:  return 0
#         pos = [0]  # mono increasing stk. keep popping if current number is smaller than than the prev one.
#         #assuming current bar is the threshold, and check what is the max area.
#         #if there's smaller bar before it, keep the smaller bar as is
#         #if there's smaller bar after it, this bar will be removed when meet the smaller bar, as the smaller bar will become the new threshold
#         output = 0
#         r = 1
#         while r < len(heights):
#             curr = heights[r]
#             while pos and heights[pos[-1]] > curr:
#                 P = pos.pop()  # previous max position
#                 W = r if pos == [] else r - (pos[-1] + 1)
#                 H = heights[P]
#                 output = max(output, W * H)
#             pos.append(r)
#             r += 1

#         while pos:
#             P = pos.pop()
#             W = r if pos == [] else r - (pos[-1] + 1)
#             H = heights[P]
#             output = max(output, W * H)
#         return output


