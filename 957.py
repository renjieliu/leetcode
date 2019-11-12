class Solution:
    def prisonAfterNDays(cells: 'List[int]', N: int) -> 'List[int]':
        def findNext(in_cell):
            output = [0]  # the start number is 0, per problem description
            for i in range(1, len(in_cell) - 1):
                if in_cell[i - 1] == in_cell[i + 1]:
                    output.append(1)
                else:
                    output.append(0)
            output.append(0)  # add the last number back , it will be 0 anyway
            return output

            # the idea is to starting from which number , it starts repeating.

        pattern = []
        pattern.append(cells)
        if N == 1:
            return findNext(cells)
        else:
            i = 0
            curr = cells
            while i < N:
                curr = findNext(curr)
                if curr not in pattern:
                    pattern.append(curr)
                else:
                    rep_start = pattern.index(curr)  # get the start position
                    rep_arr = pattern[rep_start:]
                    real_N = N - rep_start  # if the repeat does not start from the initial form, need to take out the first a few
                    pos = real_N % len(rep_arr)
                    return rep_arr[pos]

                i += 1

            return curr
