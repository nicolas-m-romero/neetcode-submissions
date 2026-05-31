class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = "".join(s.split(" "))

        left = 0
        right = len(words) - 1

        while left < right:
            if not words[left].isalnum():
                left += 1
            if not words[right].isalnum():
                right -= 1
            elif words[left].lower() != words[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
