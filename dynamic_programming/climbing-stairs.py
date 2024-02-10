# link: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climb_stairs(self, n: int, step=0, cache=None) -> int:
        if step == n:
            return 1
        elif step > n:
            return 0
        if cache is None:
            cache = {}
        elif step in cache:
            return cache[step]

        x = self.climb_stairs(n, step + 1, cache)
        cache[step + 1] = x
        y = self.climb_stairs(n, step + 2, cache)
        cache[step + 2] = y

        return x + y

