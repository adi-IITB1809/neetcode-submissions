class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Edge case: if there's only 1 person and no trust array
        if n == 1 and not trust:
            return 1
            
        # Lists to store incoming and outgoing trust counts for people 1 to n
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)
        
        # Populate the counts from the trust list
        for a, b in trust:
            outgoing[a] += 1  # person 'a' trusts someone
            incoming[b] += 1  # person 'b' is trusted by someone
            
        # Check every person from 1 to n to find the judge
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
                
        return -1