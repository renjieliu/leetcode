class Solution:
    def maxProduct(self, words: 'List[str]') -> int:
        output = 0
        arr = []
        for w in words:
            arr.append(set(w))
        for i in range (len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] & arr[j] == set():
                    output = max(output, len(words[i]) * len(words[j]))
        return output
