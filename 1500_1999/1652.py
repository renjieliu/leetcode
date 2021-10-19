class Solution:
    def decrypt(self, code: 'List[int]', k: int) -> 'List[int]':
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            code = code + code
            arr = []
            for i in range(len(code) // 2):
                arr.append(sum(code[i + 1:i + 1 + k]))
            return arr

        elif k < 0:
            start = len(code)
            code = code + code
            arr = []
            for i in range(start, len(code)):
                arr.append(sum(code[i + k:i]))
            return arr