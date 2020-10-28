class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        if nums == []: return []
        output = []
        start = nums[0]
        prev = nums[0]
        for n in nums[1:]:
            if n != prev + 1:
                post = ("->" + str(prev)) if prev != start else ""
                output.append(str(start) + post)
                start = n
                prev = n
            else:
                prev = n

        post = ("->" + str(prev)) if prev != start else ""
        output.append(str(start) + post)
        return output
