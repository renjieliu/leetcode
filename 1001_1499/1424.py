class Solution:
    def findDiagonalOrder(self, nums: 'List[List[int]]') -> 'List[int]':
        output = []
        r = curr = dropped = 0  # curr increases by 1 each time. dropped counts how many lines have been taken out.
        while nums:
            r = min(len(nums) - 1, curr - dropped)  # curr-dropped is the actual starting index
            while r > -1:
                output.append(nums[r].pop(0))
                if nums[r] == []:
                    del nums[r]
                    dropped += 1
                r -= 1
            curr += 1
        return output


