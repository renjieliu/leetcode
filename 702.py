class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        s = 0
        e = 2147483647
        while s <= e:  # bin search to find the length
            mid = (s + e) // 2
            if reader.get(mid) == 2147483647:
                e = mid - 1
            else:
                s = mid + 1
        pivot = s
        # binary search to find the target number
        s = 0
        e = pivot
        while s <= e:
            mid = (s + e) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                e = mid - 1
            elif reader.get(mid) < target:
                s = mid + 1
        return -1

# previous trivial solution
# class Solution:
#     def search(self, reader, target):
#         """
#         :type reader: ArrayReader
#         :type target: int
#         :rtype: int
#         """
#         i = 0
#         while reader.get(i) != target:
#             if reader.get(i) == 2147483647 or reader.get(i) > target:
#                 return -1
#             i+=1
#         return i