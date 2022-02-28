class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        if nums == []:
            return []
        output = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):  # each number, compare with the previous. If it's not prev+1, add previous segment
            if nums[i] != nums[i-1]+1:
                if start != end:
                    output.append(str(start) + "->" + str(end))
                else:
                    output.append(str(start))
                start = end = nums[i] # reset the start and end
            else:
                end = nums[i]

        return output + [(str(start) + "->" + str(end) if start != end else str(start))] # add the last part to the output

    

# previous approach

# class Solution:
#     def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
#         if nums == []: return []
#         output = []
#         start = nums[0]
#         prev = nums[0]
#         for n in nums[1:]:
#             if n != prev + 1:
#                 post = ("->" + str(prev)) if prev != start else ""
#                 output.append(str(start) + post)
#                 start = n
#                 prev = n
#             else:
#                 prev = n

#         post = ("->" + str(prev)) if prev != start else ""
#         output.append(str(start) + post)
#         return output

