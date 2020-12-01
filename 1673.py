class Solution:
    def mostCompetitive(self, nums: 'List[int]', k: int) -> 'List[int]':
        output = []
        for i, c in enumerate(nums):
            if output == []:
                output.append(c)
            else:
                if c < output[-1]:  # remaining items in the nums >= how many to be picked
                    rem_nums = len(nums) - 1 - i  # remaining items in the nums
                    rem_output = k - len(output)  # how many to be picked
                    while output and c < output[-1] and rem_nums >= rem_output:
                        output.pop(-1)
                        rem_nums = len(nums) - 1 - i
                        rem_output = k - len(output)

                if len(output) < k:
                    output.append(c)

        return output
