class Solution:
    def avoidFlood(self, rains: 'List[int]') -> 'List[int]':
        hmp = {}
        for i in range(len(rains)):
            r = rains[i]
            if r != 0:
                if r not in hmp:
                    hmp[r] = []
                hmp[r].append(i)

        priority = []
        output = []
        stk = set()
        arbi = 9999  # an arbitary number
        for i in range(len(rains)):
            r = rains[i]
            if r != 0:
                if r not in stk:
                    hmp[r].pop(0)
                    stk.add(r)
                    if hmp[r]:  # it will rain in the future
                        heapq.heappush(priority, hmp[r][0])
                    output.append(-1)
                else:
                    return []

            elif r == 0:
                if len(stk) == 0 or len(
                        priority) == 0:  # current stk is blank, and non of the lake will rain in the future
                    output.append(arbi)
                else:
                    v = rains[heapq.heappop(priority)]  # the first lake to rain in the future
                    stk.remove(v)
                    output.append(v)

        return output
