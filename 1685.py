class Solution:
    def getSumAbsoluteDifferences(self, nums: 'List[int]') -> 'List[int]':
        output = [sum([abs(nums[0] - n) for n in nums[1:]])]  # the first element

        for i in range(1, len(
                nums)):  # previous result + diff * left(as it's increasing) - diff*right(the diff is decreasing) - curr number and add back the previous number
            delta = nums[i] - nums[i - 1]
            leftCnt = i
            rightCnt = len(nums) - (i + 1)
            curr = output[-1] + leftCnt * delta - rightCnt * delta - nums[i] + nums[i - 1]
            output.append(curr)
        return output
