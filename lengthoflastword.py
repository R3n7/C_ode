#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.split()[-1] != ' ':
            return len(s.split()[-1])
        else:
            lengthOfLastWord(s[:-1])
