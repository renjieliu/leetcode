class Solution:
    def letterCasePermutation(self, S: str) -> 'List[str]':
        s = S.lower()
        arr = [] #all the letters
        for i, c in enumerate(s):
            if c >='a':
                arr.append(i)

        change = [] #the combination of letter positions, to be upper'ed
        def combo(change, arr, curr, n):
            if len(curr) == n:
                change.append(curr)
            else:
                for i in range(len(arr)):
                    combo(change, arr[i+1:], curr+[arr[i]], n)

        for i in range(1, len(arr)+1):
            combo(change, arr, [], i)

        res = [s] # initialize the res with all lowercase'd string
        for curr in change:
            temp = list(s)
            for pos in curr:
                temp[pos]=temp[pos].upper()
            res.append(''.join(temp))
        return res