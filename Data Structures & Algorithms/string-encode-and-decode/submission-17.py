class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for strings in strs:
            s += str(len(strings)) + '#' + strings
        return s

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            arr.append(s[i : i + length])
            i += length
        return arr