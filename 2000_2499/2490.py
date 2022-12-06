class Solution:
    def isCircularSentence(self, sentence: str) -> bool: # O( N | N )
        arr = sentence.split(' ')
        if len(arr) == 1: # only 1 word in the sentence
            return arr[0][0] == arr[0][-1]
        else:
            for i in range(1, len(arr)):
                if arr[i][0] != arr[i-1][-1]: #if current first letter is the same as the previous last letter
                    return False
            return sentence[-1] == sentence[0] # if the last letter in the sentence is the same as the first letter
    
    
