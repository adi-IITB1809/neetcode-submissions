class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n= len(people)
        people.sort()
        x = 0
        y = 0
        right=n-1
        left=0
        while left <= right:
            if people[right]+people[left]<=limit:
                x+=1
                right-=1
                left+=1

            else:
                y+=1
                right-=1

        '''if n%2 == 1:  # Not needed
            if y%2 == 0:
                y+=1'''

        return (x+y)

''' CHAT GPT SOLUTION

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats'''
