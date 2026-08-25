class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=[]
        for i in operations:
            if i not in ['+', 'C', 'D']:
                ops.append(int(i))
            elif i == '+':
                ops.append(int(ops[-1])+int(ops[-2]))
            elif i == 'D':
                ops.append(2*int(ops[-1]))
            elif i == 'C':
                ops.pop()

        return sum(ops)