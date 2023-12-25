# link: https://leetcode.com/problems/backspace-string-compare/description/

# brute-force Time: O(a+b+n), Space: O(1)
def get_typed_str(string: str):
    result = ""
    for char in string:
        if char == "#":
            result = result[: -1]
        else:
            result += char
    return result

def backspace_compare(str1: str, str2: str):
    str1 = get_typed_str(str1)
    str2 = get_typed_str(str2)

    if len(str1) != len(str2):
        return False

    for idx, char in enumerate(str1):
        char2 = str2[idx]
        if char != char2:
            return False

    return True


# optimal Time: O(max(a, b)), Space: O(n)
def get_last_typed_char_idx(string: str, idx) -> int:
    skip = 0
    while idx >= 0:
        if string[idx] == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            break
        idx -= 1
    return idx
def backspace_compare(str1: str, str2: str):
    str1_idx = len(str1) - 1
    str2_idx = len(str2) - 1

    while str1_idx >= 0 or str2_idx >= 0:
        str1_idx = get_last_typed_char_idx(str1, str1_idx)
        str2_idx = get_last_typed_char_idx(str2, str2_idx)

        str1_char = str1[str1_idx] if str1_idx >= 0 else None
        str2_char = str2[str2_idx] if str2_idx >= 0 else None

        str1_idx -= 1
        str2_idx -= 1

        if str1_char != str2_char:
            return False

    return True

