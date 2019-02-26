def isAlienSorted(words: 'List[str]', order: 'str'):
    cnt =1
    map = {}

    for i in order:
        map[i] = cnt
        cnt +=1

    for i in range(1, len(words)):
        commonStart = 0
        for j in range(0,  len(words[i-1])):
            if commonStart == len(words[i]):
                return False

            if map[words[i-1][j]] < map[words[i][j]]:
                break

            elif map[words[i-1][j]] > map[words[i][j] ]:
                return False

            elif map[words[i-1][j]] == map[words[i][j] ]:
                commonStart +=1
                continue

            if len(words[i-1]) > len(words[i]):
                return False

    return True

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
print(isAlienSorted(["ubg","kwh"], "qcipyamwvdjtesbghlorufnkzx"))
print(isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"))
print(isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))


