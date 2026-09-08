class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        max_f = max(freq)
        if max_f > (len(s) + 1)//2: return ""

        res = []
        while len(res) < len(s):
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0: continue

            tmp = freq[maxIdx]
            freq[maxIdx] = float("-inf")
            nextMax = freq.index(max(freq))
            char = chr(nextMax + ord('a'))
            res.append(char)
            freq[maxIdx] = tmp
            freq[nextMax] -= 1
        return ''.join(res)