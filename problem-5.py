	class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[i+extraCandies for i in candies]
        b=[]
        for i in l:
            if i>=max(candies):
                b.append(True)
            else:
                b.append(False)
        return b





