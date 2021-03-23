class Solution:
    def threeSumMulti(self, arr: 'List[int]', target: int) -> int:
        hmp = {}
        mod = 10**9+7
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a]+=1
        fact = lambda x: 1 if x <= 1 else x*fact(x-1)
        combo = lambda m, n: fact(m)//(fact(n) * fact(m-n))
        sig = lambda x:'-'.join([str(_) for _ in sorted(x)])
        cnt = 0
        stk = list(hmp.keys())
        seen = set()
        for i in range(len(stk)):
            a = stk[i]
            if target == a*3 and hmp[a] >=3:
                cnt += combo(hmp[a], 3)
                seen.add(sig([a,a,a]))
            else:
                for j in range(i+1, len(stk)):
                    b = stk[j]
                    c = target - a-b
                    if c in hmp and sig([a,b,c]) not in seen:
                        if a == c:
                            cnt += combo(hmp[a], 2) * combo(hmp[b], 1)
                        elif b == c:
                            cnt += combo(hmp[b], 2) * combo(hmp[a], 1)
                        else:
                            cnt += combo(hmp[a], 1) * combo(hmp[b], 1)* combo(hmp[c], 1)
                        seen.add(sig([a,b,c]))

        return cnt % mod