def find_lengthest_sub_string(str):
    start, prob, max_length = 0, 0, 1
    if len(str) == 0:
        return 0
    while start < len(str):
        prob = start + 1
        current_length = 1
        while prob < len(str) and str[prob] not in str[start: prob]:
            current_length += 1
            prob += 1
            if current_length > max_length:
                max_length = current_length
        start = prob
    return max_length

def length_of_longest_substring(s):
    # start, max_length = 0, 0
    # start_positions = {}
    # for prob in range(len(str)):
    #     if str[prob] in start_positions and start <= start_positions[str[prob]]:
    #         start = start_positions[str[prob]] + 1
    #     else:
    #         max_length = max(max_length, prob - start + 1)
    #     start_positions[str[prob]] = prob
    # return max_length
    start, max_length = 0, 0
    start_position = [-1] * 128
    for prob in range(len(s)):
        if start_position[ord(s[prob])] >= 0 and start <= start_position[ord(s[prob])]:
            start = start_position[ord(s[prob])] + 1
        else:
            max_length = max(max_length, prob - start + 1)
        start_position[ord(s[prob])] = prob
    return max_length    


str = "abcabcbb"
print(length_of_longest_substring(str))