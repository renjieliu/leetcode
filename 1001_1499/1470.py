class Solution:
    def shuffle(self, nums: 'List[int]', n: int) -> 'List[int]':
        output = []
        for i in list(zip(nums[:n], nums[n:])):
            output.append(i[0])
            output.append(i[1])
        return output