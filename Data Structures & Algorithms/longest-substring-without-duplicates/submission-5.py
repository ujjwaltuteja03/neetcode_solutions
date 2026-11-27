class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        if n == 1: return 1
        res = 1

        for i in range(n):
            cur = set()
            cur.add(s[i])
            for j in range(i+1, n):
                if s[j] in cur:
                    res = max(res, len(cur))
                    break
                cur.add(s[j])
        return res