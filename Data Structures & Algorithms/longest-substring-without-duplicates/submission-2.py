class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr= set()   
        n= len(s)
        n_max= 0
        right= 0
        left= 0
        for right in range(len(s)):

            while s[right] in arr:
                arr.remove(s[left])
                left += 1

            arr.add(s[right])

            n_max = max(n_max, right - left + 1)

        return n_max