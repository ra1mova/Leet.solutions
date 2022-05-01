class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(set(s))==len(s):
            return -1
        else:
            i,l=0,[]
            while i<len(s):
                j=len(s)-1
                while j>=0:
                    if s[i]!=s[j]:
                        j-=1
                    else:
                        l.append(j-(i+1))
                        break 
                i+=1    
        return max(l)




















