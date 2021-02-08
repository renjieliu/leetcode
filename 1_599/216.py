def combinationSum3(k: int, n: int):
    def dfs(output, curr_arr, candidates,target,target_len, curr_index):
        if sum(curr_arr) ==target and len(curr_arr)==target_len:
            output.append(curr_arr.copy())
            return -1

        for i in range(curr_index, len(candidates)):
            if len(curr_arr) >= target_len or sum(curr_arr) > target:
                break

            curr_arr.append(candidates[i])
            _ = dfs(output,curr_arr, candidates, target, target_len, i+1)
            curr_arr.pop()

        return -1


    if n <= 0:
        return []
    else:
        output = []
        _ = dfs(output,[], range(1,10), n, k, 0)
        return output

print(combinationSum3(3,7))
print(combinationSum3(3,9))