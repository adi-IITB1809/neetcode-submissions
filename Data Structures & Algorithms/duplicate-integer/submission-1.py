class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        hash = set()
        for i in range(n):
            hash.add(nums[i])

        if len(hash)!=n:
            return True

        else:
             return False