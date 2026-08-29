class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        
        sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_keys[:k]