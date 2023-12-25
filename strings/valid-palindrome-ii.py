# link: https://leetcode.com/problems/valid-palindrome-ii/

def valid_palindrome(s: str) -> bool:
    left_idx = 0
    right_idx = len(s) - 1
    to_try = None

    while left_idx <= right_idx:
        if s[left_idx] != s[right_idx]:
            if to_try is None:
                to_try = []
                if s[left_idx + 1] == s[right_idx]:
                    to_try.append((left_idx + 1, right_idx))
                if s[right_idx - 1] == s[left_idx]:
                    to_try.append((left_idx, right_idx - 1))
            if not to_try: return False
            left_idx, right_idx = to_try.pop()
            continue

        left_idx += 1
        right_idx -= 1
    return True




print(valid_palindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))