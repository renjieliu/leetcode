class Solution:
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        def tofindMax(A, end):
            loc = 0
            m = A[0]  # find the last max value location.
            i = 0
            while i <= end:
                if A[i] >= m:
                    loc = i
                    m = A[i]
                i += 1
            return loc

        output = []
        ref = sorted(A.copy())
        end = len(A) - 1  #
        while A != ref:
            loc = tofindMax(A, end)
            if loc == end:  # the number is in the good location, move the right end -1
                end -= 1
            else:
                A = A[:loc + 1][::-1] + A[loc + 1:]
                A = A[:end + 1][::-1] + A[end + 1:]
                output.append(loc + 1)  # flip the first xx
                output.append(end + 1)  # flip the whole, to make the max to the end.
                end -= 1
        return output



