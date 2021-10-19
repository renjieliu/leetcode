class Solution:
    def largestNumber(self, nums: 'List[int]') -> str:
        arr = []
        maxLength = 0
        for n in nums:
            curr = str(n)
            arr.append(curr)
            maxLength = max(maxLength,len(curr))
        # for the ones like[121, 12], [847, 84] --> repeat the max(firstCharacter , lastCharacter) for sorting
        arr.sort(key = lambda x: x + max(x[-1], x[0]) * (maxLength - len(x)) , reverse = True)
        ans = ''.join(arr).lstrip('0')
        return ans if ans else '0'

#previous approach
# class Solution:
#     def largestNumber(self, nums: 'List[int]') -> str:
#         if nums == []: return ""
#         ref = [str(_) for _ in nums]
#         w = max(map(lambda x: len(str(x)), ref))  # get the widest from the input
#         temp = sorted(ref, key=lambda x: (x * w)[:w + 1], reverse=True)  # pad it to the full length.
#         return '0' if ''.join(temp).lstrip('0') == '' else ''.join(temp).lstrip('0')
