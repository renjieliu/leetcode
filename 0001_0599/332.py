class Solution:
    def findItinerary(self, tickets: 'List[List[str]]') -> 'List[str]':
        def dfs(path, used, limit, from_to, curr, total):
            if len(path) == total:
                return path
            else:
                for c in from_to[curr]:
                    if c in from_to:
                        if used[(curr, c)] < limit[(curr, c)]:
                            used[(curr, c)] += 1
                            ans = dfs(path + [c], used, limit, from_to, c, total)
                            used[(curr, c)] -= 1
                            if ans != None and len(ans) == total: return ans
                    elif len(path + [c]) == total:
                        return path + [c]

        if tickets == []:
            return []
        else:
            used = {}
            limit = {}
            from_to = {}
            for f, t in sorted(tickets, key=lambda x: x[1]):
                if f not in from_to:
                    from_to[f] = []
                from_to[f].append(t)

                used[(f, t)] = 0
                if (f, t) not in limit:
                    limit[(f, t)] = 0
                limit[(f, t)] += 1
            #             print(limit)
            #             print(used)

            # print(from_to)

            # print(output)
            return dfs(['JFK'], used, limit, from_to, 'JFK', len(tickets) + 1)







