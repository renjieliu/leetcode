class Solution:
    def construct2DArray(self, original: 'List[int]', m: int, n: int) -> 'List[List[int]]':
        if len(original) != m*n:
            return []
        else:
            output = [[]]
            while original:
                output[-1].append(original.pop(0))
                if len(output[-1]) == n and original:
                    output.append([])
            return output



