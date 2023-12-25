# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# optimal Time: O(2n) because of setting i back to a smaller value, Space: O(m) m being the max length returned
def length_of_longest_substring(s: str) -> int:
    seen = {}
    max_len = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in seen:
            i = seen[c] + 1
            max_len = max(max_len, len(seen))
            seen = {}
        else:
            seen[c] = i
            i += 1
    return max(max_len, len(seen))

# optimal Time: O(n), Space: O(n)
def length_of_longest_substring(s: str) -> int:
    seen = {}
    max_len = 0
    curr_sub_str_idx = [0, -1]

    for idx, char in enumerate(s):
        if char in seen and seen[char] >= curr_sub_str_idx[0]:
            curr_len = curr_sub_str_idx[1] - curr_sub_str_idx[0] + 1
            max_len = max(max_len, curr_len)
            curr_sub_str_idx[0] = seen[char] + 1

        seen[char] = idx
        curr_sub_str_idx[1] = idx

    curr_len = curr_sub_str_idx[1] - curr_sub_str_idx[0] + 1
    return max(max_len, curr_len)

print(length_of_longest_substring("abcabcbb"))