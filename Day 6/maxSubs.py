class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = {}
        max_length = -1

        for i, ch in enumerate(s):
            if ch in indices:
                max_length = max(max_length, i - indices[ch] - 1)
            else:
                indices[ch] = i

        return max_length