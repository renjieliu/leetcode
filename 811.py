def clean(s):
    output = {}
    cnt = len (s) - len(s.replace(".",""))
    point = int(str(s).split(" ")[0])
    if cnt == 1:
        output[str(s).split(" ")[1]] = point
        output[str(s).split(" ")[1].split(".")[1]] = point
    if cnt ==2:
        output[str(s).split(" ")[1]] = point
        output[str(s).split(" ")[1].split(".")[1] + "." + str(s).split(" ")[1].split(".")[2]] = point
        output[str(s).split(" ")[1].split(".")[2]] = point

    return output

def subdomainVisits(cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    map = {}
    for i in cpdomains:
        for k, v in clean(i).items():
            if k in map:
                map[k] += v
            else:
                map[k] = v

    output = list()

    for k, v in map.items():
        output.append(str(v) + " " + k)

    return output

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))


