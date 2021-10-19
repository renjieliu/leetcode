class Solution:
    def lenLongestFibSubseq(self, A: 'List[int]') -> int:
        def binSearch(arr, s, e, target):
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return -1  # not found

        output = []
        len_A = len(A)
        for i in range(len_A):
            X = A[i]
            currMax = 0
            for j in range(i + 1, len_A):  # to find if X+Y exists in the array
                cnt = 0
                Y = A[j]
                loc = binSearch(A, j + 1, len_A - 1, X + Y)
                while loc != -1:  # it finds a match
                    cnt += 1
                    X = Y
                    Y = A[loc]
                    if loc != len(A) - 1:
                        loc = binSearch(A, loc + 1, len_A - 1, X + Y)
                    else:
                        break
                currMax = max(currMax, cnt)
                X = A[i]
            output.append(currMax)
        t = max(output)
        return 0 if t == 0 else t + 2

