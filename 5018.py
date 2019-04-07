def camelMatch(queries: 'List[str]', pattern: str):
    output = []
    for i in queries:
        temp = i
        wrong = 0
        for j in pattern:
            pos = temp.find(j)
            if pos == -1:
                output.append(False)
                wrong = 1
                break
            else:
                if 65 <= ord(j) <= 90:
                    for x in range(pos):
                        if 65 <= ord(temp[x]) <= 90:
                            wrong = 1
                            break
                    if wrong == 1:
                        output.append(False)
                        break
                    else:
                        temp = temp[pos + 1:]
                else:
                    temp = temp[pos + 1:]

        if wrong == 0:
            for x in temp:
                if 65 <= ord(x) <= 90:
                    wrong = 1
                    output.append(False)
                    break
        if wrong ==0:
            output.append(True)

    return output


print(camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
#
print(camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa"))
print(camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBaT"))
print(
    camelMatch(queries=["CompetitiveProgramming", "CounterPick", "ControlPanel"], pattern="CooP"))  # [false,false,true]
print(camelMatch(queries=["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn",
                          "ksvsjLctikgnTzqn", "knzsvzjLiknTszqn"], pattern="ksvjLiknTzqn"))
# True
