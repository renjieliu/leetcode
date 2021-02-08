class Solution:
    def findMissingRanges(self, nums: 'List[int]', lower: int, upper: int) -> 'List[str]':
        if nums == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]

        output = []
        if nums[0] != lower:
            if nums[0] == lower + 1:
                output.append(str(lower))
            else:
                output.append(str(lower) + "->" + str(nums[0] - 1))

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                currStart = nums[i - 1] + 1
                currEnd = nums[i] - 1
                if currStart == currEnd:
                    output.append(str(currStart))
                else:
                    output.append(str(currStart) + "->" + str(currEnd))

        if nums[-1] != upper:
            if nums[-1] == upper - 1:
                output.append(str(upper))
            else:
                output.append(str(nums[-1] + 1) + "->" + str(upper))

        return output