class Solution:
    def expand(self, S: str) -> 'List[str]':
        def expand(A, B):  # cross join A with B
            if A == []:
                A.append("")
            if B == []:
                B.append("")
            output = []
            for a in A:
                for b in B:
                    output.append(a + b)
            return output

        stk = 0
        pool = []
        for s in S:  # push all the character to the pool, if standalone,  [x], if optional, [a,b,c], then cartesian join all.
            if s != ",":
                if s == "{":
                    stk = 1
                    pool.append([])
                elif s == "}":
                    stk = 0
                else:
                    if stk == 1:
                        pool[-1].append(s)
                    else:
                        pool.append([s])

        while len(pool) > 1:
            t = expand(pool[0], pool[1])
            pool.pop(0)
            pool.pop(0)
            pool.insert(0, t)

        return sorted(pool[0])




