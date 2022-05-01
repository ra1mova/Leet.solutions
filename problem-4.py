class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] +=1

        if len(dic.values())==len(set(dic.values())):
            return True
        return False




