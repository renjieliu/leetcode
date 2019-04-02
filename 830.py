def largeGroupPositions(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    output = []
    cnt = 1
    for i in range(0, len(S)-1):
        if S[i] == S[i+1]:
            cnt +=1
        else:
            if cnt >= 3:
                output.append([i-cnt+1, i])
            cnt = 1

    if cnt >= 3: #this is for the last matched group
        output.append([len(S)-1 - cnt + 1, len(S)-1])

    return output

print(largeGroupPositions("abbxxxxzzy"))
print(largeGroupPositions("abcdddeeeeaabbbcd"))
print(largeGroupPositions("abc"))
print(largeGroupPositions("aaa"))




