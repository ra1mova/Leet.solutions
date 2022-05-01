class Solution(object):
    def kthFactor(self, n, k):
        l=[i  for i in range(1, n+1) if n%i==0]
        if len(l)<k:
            return -1
        else:
            return l[k-1]














