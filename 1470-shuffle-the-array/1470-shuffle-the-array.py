class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # * Shuffle the Array — LeetCode #1470
        # * Interleave first and second halves → zip index i with i+n | O(n) time
        res = []
        for i in range(n):
            res.append(nums[i])       # ! xi → first half
            res.append(nums[i + n])   # ! yi → second half
        return res