class Solution:
    def canReach(self, arr: 'List[int]', start: int) -> bool:
        def dfs(check, curr_pos, dp, start):
            # print(curr_pos)
            if curr_pos == start:
                return 1
            elif dp[curr_pos] == [] or check[curr_pos] == 1:
                return 0
            else:
                check[curr_pos] = 1
                for i in dp[curr_pos]:  # in order to reach t,  find all the possible source for t
                    if dfs(check, i, dp, start) == 1:
                        return 1
                return 0

        target = []
        check = [0 for _ in range(len(arr))]  # to avoid [1,1,1,1], which could cause infinite loop
        dp = [[] for _ in range(len(arr))]  # hold the possible source to reach current position
        for i in range(len(arr)):
            if arr[i] == 0:
                target.append(i)
            else:
                if -1 < arr[i] + i < len(arr):
                    dp[arr[i] + i].append(i)
                if -1 < i - arr[i] < len(arr):
                    dp[i - arr[i]].append(i)
        # print(target, '--- ' , dp)
        if target == []:
            return False
        else:
            for t in target:  # all the 0's in the arr
                if dfs(check, t, dp, start) == 1:
                    return True
            return False






































