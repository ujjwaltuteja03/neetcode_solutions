class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #brute force

        # def dfs(i):
        #     if i == len(s): return True
        #     for w in wordDict:
        #         if ((i+len(w)) <= len(s) and
        #             s[i : i + len(w)] == w):
        #             if dfs(i+len(w)):
        #                 return True
        #     return False
        # return dfs(0)

        #hash set

        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s): return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1): return True

            return False

        return dfs(0)