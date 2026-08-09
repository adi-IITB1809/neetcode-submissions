class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        ''' My Soution with time complexity O(n*k)
            for i in range(k):
            nums.insert(0, nums[n-1])
            nums.pop(n)'''