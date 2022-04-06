class Solution:
    def threeSumMulti(self, arr: 'List[int]', target: int) -> int: # O(N2LogN | N)
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1
        output = 0
        arr = sorted(hmp.keys())
        seen = set()
        fact = lambda x: 1 if x <= 1 else x * fact(x-1)
        combo = lambda x, y: fact(x)//(fact(y) * fact(x-y))
        for i in range(len(arr)):
            for j in range(len(arr)-1, i-1, -1):
                a = arr[i]
                b = target-arr[i]-arr[j]
                c = arr[j]
                t = tuple(sorted([a, b, c]))
                if b in hmp and t not in seen: 
                    seen.add(t)
                    cnt = {} #how many times the number needs to be picked. for case like (2,3,3), or (3,3,3)
                    for x in [a, b , c]: 
                        if x not in cnt:
                            cnt[x] = 0
                        cnt[x] += 1
                    curr = 1
                    for k, v in cnt.items():
                        curr *= combo(hmp[k], v)
                    output += curr
                    
        return output%(10**9+7)
                

# previous solution

# class Solution:
#     def threeSumMulti(self, arr: 'List[int]', target: int) -> int:
#         hmp = {}
#         mod = 10**9+7
#         for a in arr:
#             if a not in hmp:
#                 hmp[a] = 0
#             hmp[a]+=1
#         fact = lambda x: 1 if x <= 1 else x*fact(x-1)
#         combo = lambda m, n: fact(m)//(fact(n) * fact(m-n))
#         sig = lambda x:'-'.join([str(_) for _ in sorted(x)])
#         cnt = 0
#         stk = list(hmp.keys())
#         seen = set()
#         for i in range(len(stk)):
#             a = stk[i]
#             if target == a*3 and hmp[a] >=3:
#                 cnt += combo(hmp[a], 3)
#                 seen.add(sig([a,a,a]))
#             else:
#                 for j in range(i+1, len(stk)):
#                     b = stk[j]
#                     c = target - a-b
#                     if c in hmp and sig([a,b,c]) not in seen:
#                         if a == c:
#                             cnt += combo(hmp[a], 2) * combo(hmp[b], 1)
#                         elif b == c:
#                             cnt += combo(hmp[b], 2) * combo(hmp[a], 1)
#                         else:
#                             cnt += combo(hmp[a], 1) * combo(hmp[b], 1)* combo(hmp[c], 1)
#                         seen.add(sig([a,b,c]))

#         return cnt % mod



