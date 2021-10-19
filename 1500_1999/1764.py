class Solution:
    def canChoose(self, groups: 'List[List[int]]', nums: 'List[int]') -> bool:
        i = 0
        while i < len(nums) and groups: #check if current arr is same as the current compared group
            compare = groups[0]
            if nums[i: i+len(compare)] == compare:
                i += len(compare)
                groups.pop(0)
                if groups == []:
                    return True
            else:
                i+=1
        return False
