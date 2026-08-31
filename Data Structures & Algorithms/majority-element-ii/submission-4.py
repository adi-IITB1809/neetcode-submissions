class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first= None
        second= None
        first_count= 0
        second_count= 0
        for i in range(len(nums)):
            if nums[i]== first:
                first_count+=1

            elif nums[i]== second:
                second_count+=1

            elif first_count==0:
                first= nums[i]
                first_count=1

            elif second_count==0:
                second= nums[i]
                second_count=1

            else:
                first_count-=1
                second_count-=1
     # Check actual frequency
        first_count = 0
        second_count = 0

        for i in range(len(nums)):
            if nums[i] == first:
                first_count += 1
            elif nums[i] == second:
                second_count += 1

        ans = []

        if first_count > len(nums)//3:
            ans.append(first)

        if second_count > len(nums)//3:
            ans.append(second)

        return ans