class Solution:
    def decodeString(self, s: str) -> str:
        strings = []
        counts = []
        cur = ""
        k=0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                strings.append(cur)
                counts.append(k)
                cur=""
                k=0
            elif c == "]":
                temp = cur
                cur = strings.pop()
                count = counts.pop()
                cur += temp*count
            else:
                cur+=c
        return cur