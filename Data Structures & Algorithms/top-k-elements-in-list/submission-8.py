'''class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        
        sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_keys[:k]'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        # Count frequency
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        # Create buckets
        bucket = [[] for i in range(len(nums) + 1)]

        # Put numbers into buckets according to frequency
        for num in hashmap:
            frequency = hashmap[num]
            bucket[frequency].append(num)

        arr = []

        # Start from highest frequency
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                arr.append(num)

                if len(arr) == k:
                    return arr