class Solution(object):
    def threeEqualParts(self, A):
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T + 1, 2 * T + 1}:
                    breaks.append(i)
                if su in {T, 2 * T, 3 * T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not (A[i1:j1 + 1] == A[i2:j2 + 1] == A[i3:j3 + 1]):
            return [-1, -1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2 + 1]



