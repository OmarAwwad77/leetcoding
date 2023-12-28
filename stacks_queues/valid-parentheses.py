# link: https://leetcode.com/problems/valid-parentheses/description/

def is_valid(s: str) -> bool:
    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    to_close = []
    for c in s:
        if c in parentheses:
            to_close.append(c)
        else:
            last_c = to_close.pop() if to_close else None
            if not parentheses.get(last_c) == c:
                return False

    return False if to_close else True

