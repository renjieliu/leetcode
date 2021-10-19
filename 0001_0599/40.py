def combinationSum2(candidates: 'List[int]', target: int):
    def dfs(output, curr_arr, candidates, target, curr_index):
        if sum(curr_arr) == target:
            if curr_arr not in output:
                output.append(curr_arr.copy())
            return -1
        else:
            for i in range(curr_index, len(candidates)):
                if sum(curr_arr) > target:
                    break
                curr_arr.append(candidates[i])
                _ = dfs(output, curr_arr, candidates, target, i+1)
                curr_arr.pop()

            return -1

    if candidates ==[]:
        return []
    else:
        output = []
        candidates.sort()
        _ = dfs(output, [], candidates, target, 0)
        return output




print(combinationSum2([10,1,2,7,6,1,5], target = 8))
print(combinationSum2(candidates = [2,5,2,1,2], target = 5))
print(combinationSum2(candidates = [1,2], target = 4))