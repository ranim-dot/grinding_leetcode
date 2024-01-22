class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringModified = re.sub(r'[^a-zA-Z0-9]', '', s).casefold()

        return stringModified == stringModified[::-1]