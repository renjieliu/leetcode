class Solution:
    def largestOverlap(self, A: 'List[List[int]]', B: 'List[List[int]]') -> int:
        def shift(x, y, im1, im2, dim):
            output = 0
            for row1, row2 in enumerate(range(y, dim)):
                for col1, col2 in enumerate(range(x, dim)):
                    output += 1 if im1[row1][col1] == 1 and im1[row1][col1] == im2[row2][col2] else 0
            return output

        max_overlap = 0

        for x in range(len(A)):
            for y in range(len(A)):
                max_overlap = max(max_overlap, shift(x, y, A, B, len(A)))
                max_overlap = max(max_overlap, shift(x, y, B, A, len(A)))

        return max_overlap