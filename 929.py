def numUniqueEmails(emails: 'List[str]'):
    list = []
    for i in emails:
        x1 = str(i).find("@")
        t = str(i)[:x1].replace(".", "")
        x2 = t.find("+")
        if x2!=-1:
            if t[:x2]+str(i)[x1:] not in list:
                list.append(t[:x2]+str(i)[x1:])
        else:
            if t+str(i)[x1:] not in list:
                list.append(t+str(i)[x1:])

    return len(list)



print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.maisl+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))