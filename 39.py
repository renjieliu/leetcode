def combinationSum(candidates: 'List[int]', target: int):
    output = []
    curr = []
    candidates.sort()

    if candidates == []:
        return []

    def dfs(output, curr, candidates, target, currIndex = 0 ):
        if sum(curr) == target:
            output.append(curr.copy())
            return 1

        for i in range(currIndex, len(candidates)):
            if sum(curr) > target:
                break
            curr.append(candidates[i])
            x = dfs(output, curr, candidates, target, i)
            curr.pop()

    dummy = dfs(output, curr, candidates, target, 0)


    return output

print(combinationSum(candidates = [2,3,6,7], target = 7))

