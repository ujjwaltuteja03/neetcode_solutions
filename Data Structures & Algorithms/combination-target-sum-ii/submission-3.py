class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        curr=[]
        def backtrack(start, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            for i in range(start, n):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining: break
                curr.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                curr.pop() 
        

        backtrack(0, target)
        return res