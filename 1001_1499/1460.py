class Solution:
    def canBeEqual(self, target: 'List[int]', arr: 'List[int]') -> bool:
        return True if len(set(target) - set(arr)) == 0 else False