def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    output = ""
    cnt = 0
    for i in range(len(S) - 1, -1, -1):
        if S[i] != "-":
            cnt += 1
            output = S[i] + output
            if cnt == K:
                output = "-" + output
                cnt = 0
        else:
            continue

    return output.upper().strip("-")

print(licenseKeyFormatting("5F3Z-2e-9-w",4))

