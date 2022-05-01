class Solution:
    def getFolderNames(self, names): 
        ans = {}
        for w in names:
            if w in ans:
                k = ans[w] + 1
                while f"{w}({k})" in ans: k += 1
                ans[w], w = k, f"{w}({k})"
            ans[w] = 0
        return ans.keys()
















