class Solution:
    def slowestKey(self, rt: List[int], kp: str) -> str:
        l = []
        l.append([rt[0] , kp[0]])
        for i in range(1 ,len(rt)):
            l.append([rt[i] - rt[i-1] , kp[i]])
        maxs = max(l)
        return maxs[1]







