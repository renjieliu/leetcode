class Solution:
    def toHexspeak(self, num: str) -> str:
        def toHEx(N):
            output = ""
            mod = []
            while N>=16:
                mod.append(str(N%16))
                N=N//16
            mod.append(str(N))
            #print(mod)
            
            for m in mod[::-1]: 
                if m =="10":
                    output+="A"
                elif m== "11":
                    output+="B"
                elif m== "12":
                    output+="C"
                elif m =="13":
                    output+="D"
                elif m =="14":
                    output+= "E"
                elif m=="15":
                    output+="F"
                else:
                    output+=str(m)
            return output
        
        t = toHEx(int(num))
        #print(t)
        for i in [2,3,4,5,6,7,8,9]:
            if str(i) in t:
                return "ERROR"
        return t.replace("0", "O").replace("1", "I")
    
    
