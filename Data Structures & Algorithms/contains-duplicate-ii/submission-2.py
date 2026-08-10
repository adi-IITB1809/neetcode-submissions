class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i-k])

        return False


'''class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        return True

        return False '''