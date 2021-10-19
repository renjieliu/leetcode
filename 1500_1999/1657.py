class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False
        else:
            arr_a = [0]*26 #to hold occurrence of characters
            arr_b = [0]*26
            word2 = list(word2)
            base = ord('a')
            for i, c in enumerate(word1):
                arr_a[ord(c)-base ]+=1
                arr_b[ord(word2[i])-base]+=1
            if set(arr_a)!=set(arr_b): #the occurrence numbers needs to be same for them to be close
                return False
            else:
                while arr_a and arr_b:
                    a = arr_a.pop(0)
                    b = arr_b.pop(0)
                    if a*b == 0 and a+b != 0: #one of them is zero
                        return False
                return True

