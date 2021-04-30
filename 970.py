class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> 'List[int]':
        if bound < 2:
            return []
        elif x==1 or y == 1:
            m = max(x, y)
            return list({1+ m**_ for _ in range(100) if m**_+1 <=bound})
        output = set()
        a = min(x,y)
        b = max(x,y)
        for i in range(bound):
            for j in range(bound):
                t = a**i + b**j
                if t > bound:
                    break
                else:
                    output.add(t)
            if a**i > bound:
                break
        return list(output)

