class Solution:
    def closestCost(self, baseCosts: 'List[int]', toppingCosts: 'List[int]', target: int) -> int:
        dp = [[t * _ for _ in range(3)] for t in toppingCosts ] #take 0, take 1 and take 2
        def add(arr_1, arr_2):
            output = []
            for a in arr_1:
                for b in arr_2:
                    output.append(a+b)
            return output
        prev = dp[0]
        for i in range (1, len(dp)): #get all the possiblities of the total topping cost. arr_1 + arr_2
            curr = add(prev, dp[i])
            prev = curr
        cost = prev
        output = float('inf')
        diff= float('inf')
        for b in baseCosts:
            for c in cost:
                if abs(b+c-target) < diff:
                    output = b+c
                    diff = abs(b+c-target)
                elif abs(b+c-target) == diff:
                    output = min(output, b+c)
        return output





