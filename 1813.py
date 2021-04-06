class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1 if len(sentence1) <= len(sentence2) else sentence2 #the shorter one
        b = sentence1 if a == sentence2 else sentence2
        a = a.split(' ')
        b = b.split(' ')
        while a: #pop from the left
            if a[0] == b[0]:
                a.pop(0)
                b.pop(0)
            else:
                break
        while a: # pop from the right
            if a[-1] == b[-1]:
                a.pop()
                b.pop()
            else:
                break
        return a==[] #if they are similar, the shorter one should be empty after checking
