class Solution:
    def longestMountain(A: 'List[int]'):
        if len(A) < 3:
            return 0
        else:
            r = 1
            prev_up, output = 0, 0
            up = 0
            down = 0
            while r < len(A):
                if A[r] > A[r - 1]:
                    if up > 0:  # it's upping
                        up += 1
                    elif up == 0:  # it was down, now it's up
                        # output = max(prev_up+down, output)
                        down = 0
                        up = 2

                elif A[r] < A[r - 1]:
                    if down > 0:  # it's downing
                        down += 1
                        output = max(prev_up + down, output)
                    elif down == 0 and up > 0:
                        prev_up = up
                        up = 0  # it was up, now it's down
                        down = 1  # start downing, the peak point has been counted in the up, don't need to double count
                        output = max(prev_up + down, output)

                elif A[r] == A[r - 1]:
                    up = 0
                    down = 0

                r += 1

        return output
