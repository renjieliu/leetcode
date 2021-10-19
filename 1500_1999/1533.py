# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        s = 0
        e = reader.length() - 1
        while s <= e:
            if s == e:
                return s
            else:
                mid = (s + e) // 2
                if (
                        e - s + 1) % 2 == 0:  # compare on the same length , if left == right, then the mid one is the one we find.
                    result = reader.compareSub(s, mid, mid + 1, e)
                else:
                    result = reader.compareSub(s, mid, mid, e)

                if result == 0:
                    return mid

                elif result == 1:
                    e = mid
                else:
                    s = mid + 1

        return s









