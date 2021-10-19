def canMakePaliQueries(s: str, queries: 'List[List[int]]'):
    # aaa --> a remains --> 0  to be replaced
    # abcde abcde remains half of them need to be replaced.
    # aabc  --> b, c left. replace either one to make it palindrome
    def diff(d1, d2):
        cnt = 0
        for k,v in d2.items():
            x = 0
            if k in d1:
                if v-d1[k] != 0 :
                   x = v-d1[k]
            else:
                x = v

            if x%2 != 0:
                cnt += 1

        return cnt // 2


    output = []
    map = [{s[0]:1}]
    #to precalculate
    for i in range(1,len(s)):
        t = s[i]
        dict = map[-1].copy()
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
        map.append(dict)


    #main

    for i in queries:
        d1 = 0 if i[0] ==0 else i[0]-1
        temp = {} if d1 == 0 else map[d1]
        d2 = map[i[1]]
        #print(temp,'>>>',d2)
        if diff(temp, d2) <= i[2]:
            output.append(True)
        else:
            output.append(False)

    return output


print(canMakePaliQueries( s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])) #[True, False, False, True, True]
print(canMakePaliQueries( s = "hunu",  queries = [[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]])) #[True, False, True, True, True, True, True, False, True, False, True, True, True]


