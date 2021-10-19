class Solution:
    def stringMatching(self, words: 'List[str]') -> 'List[str]':
        output=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    output.append(words[i])
        return list(set(output))