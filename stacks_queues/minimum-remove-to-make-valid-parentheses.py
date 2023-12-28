# link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def min_remove_to_make_valid(s: str) -> str:
    str_list = list(s)
    parentheses = ('(', ')')
    to_close = []

    for idx, c in enumerate(str_list):
        if c in parentheses:
            if c == parentheses[0]:
                to_close.append(idx)
            else: # closing
                if not to_close:
                    str_list[idx] = None
                else:
                    to_close.pop()

    str_list = [c for idx, c in enumerate(str_list) if c and idx not in to_close]
    return ''.join(str_list)
