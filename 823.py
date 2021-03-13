class Solution:
    def numFactoredBinaryTrees(self, arr: 'List[int]') -> int:
        arr.sort()
        mod = 10**9+7
        pool = set(arr) #to reduce the lookup time to O(1)
        tree_cnt = {}
        def divisor(n): #find all the divisor of n
            output = []
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    output.append(i)
                    if n//i != i:
                        output.append(n//i)
            return output
        output = 0
        for a in arr:
            cnt_root = 1
            for d in divisor(a):
                currTree = 0
                if d in pool and a//d in pool:
                    currTree += 1
                    if d in tree_cnt: # tree number of the left divisor
                        currTree *= tree_cnt[d]
                    if a//d in tree_cnt: # tree number of the right divisor
                        currTree *= tree_cnt[a//d]
                cnt_root += currTree
            tree_cnt[a] = cnt_root
            output += cnt_root
        # print(tree_cnt)
        return output%mod