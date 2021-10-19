class Solution:
    def largestValsFromLabels(values: 'List[int]', labels: 'List[int]', num_wanted: int, use_limit: int) -> int:
        value_dict = {}  # to record all the values, and how many times each label appears
        for i in range(len(values)):
            v = values[i]
            if v not in value_dict:
                value_dict[v] = {}  # if it's first time seeing the number, create a new bucket for it.
            if labels[i] not in value_dict[v]:
                value_dict[v][labels[i]] = 0  # if the label is not seen for the number
            if value_dict[v][labels[i]] < use_limit:
                value_dict[v][labels[i]] += 1  # if the label has been seen less than the limit

        v_list = sorted(list(value_dict.keys()), reverse=True)
        label_used = {}
        picked = 0
        output = 0
        for curr_num in v_list:
            for label, curr_num_label_cnt in value_dict[curr_num].items():
                if label not in label_used:
                    label_used[label] = 0
                while label_used[
                    label] < use_limit:  # current label can still be used , and start picking from the pool
                    if picked >= num_wanted:
                        return output
                    else:
                        output += curr_num
                        label_used[label] += 1
                        picked += 1
                        curr_num_label_cnt -= 1
                        if curr_num_label_cnt == 0:
                            break

        return output