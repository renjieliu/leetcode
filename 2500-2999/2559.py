class Solution:
    def vowelStrings(self, words: 'List[str]', queries: 'List[List[int]]') -> 'List[int]': # O( N | N )
        arr = [0] # acc sum up to current
        for w in words: 
            if w[0] in "aeiou" and w[-1] in "aeiou":
                arr.append(arr[-1] +1)
            else:
                arr.append(arr[-1])
        output = []
        for s, e in queries: # curr - prev 
            output.append(arr[e+1] - arr[s])
        return output

