class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
    
        l, curr_sum, n, target, ans = 0, 0, len(nums), sum(nums)-x, -1

        if target < 0: return -1
        if target == 0: return n

        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target and l <= r:
                if curr_sum == target:
                    ans = max(ans, r-l+1)
                curr_sum -= nums[l]
                l+=1

        return n - ans if ans != -1 else -1

















