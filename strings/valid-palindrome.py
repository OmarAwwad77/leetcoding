# link: https://leetcode.com/problems/valid-palindrome/
import re

# using regex
def isPalindrome(s: str) -> bool:
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    start_idx = 0
    end_idx = len(s) - 1

    while end_idx > start_idx:
        if s[start_idx] != s[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1

    return True


# manual Time: O(n), Space(1)
def is_palindrome(s: str) -> bool:
    if not s: return True
    length = len(s)
    left_idx = 0
    right_idx = length - 1

    while not left_idx > right_idx:
        # set left_idx
        while not s[left_idx].isalnum():
            left_idx += 1
            if left_idx == length:
                return True
        # set right_idx
        while not s[right_idx].isalnum():
            right_idx -= 1
            if right_idx == -1:
                return True

        if left_idx > right_idx:
            return True
        if s[left_idx].lower() != s[right_idx].lower():
            return False

        left_idx += 1
        right_idx -= 1
    return True

