class Solution:
    def minimumLengthEncoding(self, words: 'List[str]') -> int:
        words.sort(key=lambda x: len(x))
        curr = ""
        for i in range(len(words)):  # check each words, see if it's a tail of others
            good = 1
            for j in range(i + 1, len(words)):
                # print(words[i], words[j], isTail(words[i], words[j]))
                a = words[i]
                b = words[j]
                if b[-len(a):] == a:
                    good = 0
                    break
            if good == 1:
                curr += words[i] + '#'

        # print(curr)
        return len(curr)
