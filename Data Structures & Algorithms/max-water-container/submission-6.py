class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        x=0
        # O(n)        
        left= 0
        right= n-1
        Max_area= 0
        while left<right:
            current_area= (right-left)* min(heights[right],heights[left])
            
            if current_area > Max_area:
                Max_area = current_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return Max_area


        # O(n^2)
'''      for i in range(n-1):
            for j in range(i+1,n):
                Area= min(heights[i],heights[j])*(j-i)
                if x < Area:
                    x= Area
                else: x=x

        return x
'''    
