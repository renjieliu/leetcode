class Solution:
    def decode(self, encoded: 'List[int]', first: int) -> 'List[int]':
        output = [first]
        for e in encoded:
            output.append(output[-1]^e)
        return output



