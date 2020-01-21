class Solution:
    def largestNumber(self, nums: 'List[int]') -> str:
        if nums == []: return ""
        ref = [str(_) for _ in nums]
        w = max(map(lambda x: len(str(x)), ref))  # get the widest from the input
        temp = sorted(ref, key=lambda x: (x * w)[:w + 1], reverse=True)  # pad it to the full length.
        return '0' if ''.join(temp).lstrip('0') == '' else ''.join(temp).lstrip('0')
