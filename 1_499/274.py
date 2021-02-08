class Solution:
    def hIndex(self, citations: 'List[int]') -> int:
        if citations == []:
            return 0
        hmp = {}
        e = max(citations)
        s = 0
        output = 0
        while s <= e:  # using binary search for the h index
            mid = (s + e) // 2
            hmp['at least'] = 0
            hmp['no more'] = 0
            for c in citations:
                if c > mid:
                    hmp['at least'] += 1
                elif c < mid:
                    hmp['no more'] += 1
                elif c == mid:
                    hmp['no more'] += 1
                    hmp['at least'] += 1

            if hmp['at least'] >= mid:
                output = max(output, mid)
                s = mid + 1
            else:
                e = mid - 1

        return output


