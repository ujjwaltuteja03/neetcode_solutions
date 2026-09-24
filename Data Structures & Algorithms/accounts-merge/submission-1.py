class UnionFind:
    def __init__(self, n: int):
        self.parent = [x for x in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py: return False # already connected, no new union occurs

        else:
            if self.rank[px] >= self.rank[py]:
                self.parent[py] = px
                self.rank[px] += self.rank[py]
            else:
                self.parent[px] = py
                self.rank[py] += self.rank[px]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailtoAcc = {} #email -> index of acc it first appeared
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoAcc:
                    uf.union(i, emailtoAcc[e]) # make one of the two ids parent of both
                else:
                    emailtoAcc[e] = i

        emailGroup = defaultdict(list) #index of acc -> list of emails
        for e,i in emailtoAcc.items():
            leader = uf.find(i) #use parent we updated earlier
            emailGroup[leader].append(e)
        
        res = []
        for i,emails in emailGroup.items():
            name = accounts[i][0] # i points to index of acc that the current iteration of emails belongs to
            res.append([name] + sorted(emailGroup[i]))
        return res



        