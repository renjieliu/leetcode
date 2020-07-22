class Solution:
    def mostVisitedPattern(self, username: 'List[str]', timestamp: 'List[int]', website: 'List[str]') -> 'List[str]':
        pack = sorted(list(zip(username, timestamp, website)), key=lambda x: x[1])
        username_wk = []
        website_wk = []
        for p in pack:
            username_wk.append(p[0])
            website_wk.append(p[2])

        hmp_person = {}
        for i, c in enumerate(username_wk):  # websites the person visted
            if c not in hmp_person:
                hmp_person[c] = []
            hmp_person[c].append(website_wk[i])

        hmp_seq = {}
        maxx = -float('inf')
        output = None
        person_seq = {}
        for p, v in hmp_person.items():
            if len(v) >= 3:
                if p not in person_seq:
                    person_seq[p] = []
                for i in range(len(v) + 1 - 3):
                    for j in range(i + 1, len(v) + 1 - 2):
                        for k in range(j + 1, len(v)):
                            seq = (v[i], v[j], v[
                                k])  # current 3 sequence, to check how many times it has been visited tuple(v[i:i+3])
                            if seq not in person_seq[p]:
                                person_seq[p].append(seq)
        hmp_seq = {}
        for k, v in person_seq.items():
            for c in v:
                if c not in hmp_seq:
                    hmp_seq[c] = 0
                hmp_seq[c] += 1

                if hmp_seq[c] > maxx:
                    maxx = hmp_seq[c]
                    output = c

                elif hmp_seq[c] == maxx and c < output:
                    output = c

        # print(pack)
        # print(hmp_seq)
        return list(output)


#using SQL approach
# create table visit(users varchar(10), time real, website varchar(2000))

# truncate table visit

# insert into visit values
# ('joe', 1, 'home'),
# ('joe', 2, 'about'),
# ('joe', 3, 'career'),
# ('james', 4, 'home'),
# ('james', 5, 'cart'),
# ('james', 6, 'maps'),
# ('james', 7, 'home'),
# ('mary', 8, 'home'),
# ('mary', 9, 'about'),
# ('mary', 10, 'career')


# select top 1
# v1.website + '-' + v2.website + '-' + v3.website, count(distinct v1.users)
# from visit v1 
# inner join visit v2 on v1.users = v2.users and v2.time > v1.time
# inner join visit v3 on v2.users = v3.users and v3.time > v2.time
# group by 
# v1.website + '-' + v2.website + '-' +  v3.website
# order by 2 desc , 1
    
