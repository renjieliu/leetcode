class Solution:
    def maxEqualRowsAfterFlips(matrix: 'List[List[int]]') -> int:
        # find all the changes in the current row, and record it to the hashmap.
        # As long as there's a change in the array, the column/position can be flipped.
        # Get the maximum changing-position to be flipped.
        def findDiff(arr):
            output = []
            for i in range(len(arr) - 1):
                if arr[i] != arr[i + 1]:
                    output.append(str(i))

            return "".join(output)

        diff = {}
        output = 0
        for m in matrix:
            curr = findDiff(m)
            if curr not in diff:
                diff[curr] = 0
            diff[curr] += 1
            output = max(output, diff[curr])

        return output
