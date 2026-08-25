class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speedL= 1
        speedM= max(piles)
        while speedL<=speedM:
            midSpeed= (speedL+speedM)//2
            
            totalHours = 0

            for pile in piles:
                totalHours += (pile + midSpeed - 1) // midSpeed

            if totalHours <= h:
                speedM = midSpeed - 1
            else:
                speedL = midSpeed + 1

        return speedL