class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        result = []

        for i in range(len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if len(result) == 0:
                result.append([start, end])

            else:
                last_start = result[-1][0]
                last_end = result[-1][1]

                if start <= last_end:
                    result[-1][1] = max(last_end, end)

                else:
                    result.append([start, end])

        return result