class Solution:
    def isCovered(self, ranges: 'List[List[int]]', left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])

        def find(arr, v):
            s = 0
            e = len(arr) - 1
            while s <= e:
                mid = s - (s - e) // 2
                if arr[mid][0] > v:  # if current start is greater, move to left
                    e = mid - 1
                elif arr[mid][0] <= v <= arr[mid][1]:
                    return True
                else:
                    return find(arr[:mid], v) | find(arr[mid + 1:], v)  # find left and right
            return False

        for i in range(left, right + 1):  # binary search to find if i is in the ranges
            if find(ranges, i) == False:
                return False
        return True

# previous approach
# class Solution:
#     def isCovered(self, ranges: 'List[List[int]]', left: int, right: int) -> bool:
#         cnt = 0
#         for i in range(left, right+1):
#             for a, b in ranges:
#                 if a<=i<=b:
#                     cnt += 1
#                     break
#         return cnt == right-left+1
#
