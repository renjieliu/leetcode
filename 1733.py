class Solution:
    def minimumTeachings(self, n: int, languages: 'List[List[int]]', friendships: 'List[List[int]]') -> int:
        output = float('inf')
        cantTalk = []
        languages = [set(x) for x in languages]
        for a, b in friendships:
            lang_a = languages[a - 1]
            lang_b = languages[b - 1]
            if lang_a & lang_b == set():  # if a and b cannot talk before teaching
                cantTalk.append([a, b])
        if cantTalk == []:
            return 0
        else:
            for i in range(1, n + 1):  # try all the languages, see the number of people to teach
                teach = set()
                for a, b in cantTalk:
                    if i not in languages[a - 1]:
                        teach.add(a)
                    if i not in languages[b - 1]:
                        teach.add(b)
                output = min(output, len(teach))

            return output









