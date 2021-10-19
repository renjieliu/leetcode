class Solution:
    def pathSum(self, nums: 'List[int]') -> int:
        def dfs(output, check, curr, arr, pos, findLevel, child):  # level is 1-based,while child is 0-based
            if findLevel > int(arr[-1][0]) or child[0] > 7:  # greater than the max level
                output.append(curr)
            else:
                find = 0
                for i in range(pos + 1, len(arr)):
                    if check[i] == 0 and int(arr[i][0]) == findLevel and int(
                            arr[i][1]) - 1 in child:  # child of the previous node, soucre is 1-based
                        check[i] = 1
                        find = 1
                        dfs(output, check, curr + [int(arr[i][2])], arr, i, findLevel + 1,
                            [2 * (int(arr[i][1]) - 1), 2 * (int(arr[i][1]) - 1) + 1])
                if find == 0:
                    output.append(curr)

        arr = [str(_) for _ in nums]
        output = []
        dfs(output, [0] * len(arr), [int(arr[0][2])], arr, 0, 2, [0, 1])
        # print(output)
        res = 0
        for o in output:
            res += sum(o)
        return res