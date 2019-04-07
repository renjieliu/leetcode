def videoStitching(clips: 'List[List[int]]', T: 'int'):
    clips.sort()
    arr = [-1]*(T+1)
    arr[0] = 1
    for i in range(len(clips)):
        if clips[i][0] ==0:
            for j in range(clips[i][0], clips[i][1]+1):
                if j == T:
                    return 1
                arr[j]=1
        else:
            for x in range(len(arr)): #this is to check if there's any gap.
                if x<=clips[i][0] and arr[x] ==-1:
                    return -1

            for j in range(clips[i][0], clips[i][1]+1):
                if j==T:
                    return arr[clips[i][0]]+1
                if arr[j] ==-1:
                    arr[j] = arr[clips[i][0]]+1

        #print(clips[i], arr)
    return arr[-1]

print(videoStitching( clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10))
print(videoStitching( clips = [[0,1],[1,2]], T = 5))
print(videoStitching( clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9))
print(videoStitching([[0,4],[2,8]],5))
print(videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9)) #3

print(videoStitching([[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]],2))
