#https://leetcode.com/problems/implement-strstr/submissions/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        try:
            return haystack.index(needle)
        except:
            return -1
