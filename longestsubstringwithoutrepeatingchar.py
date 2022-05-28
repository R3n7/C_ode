#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
 def lengthOfLongestSubstring(self, s: str) -> int:
        winstart=0
        char_freq={}
        maxlength=0
        for winend in range(len(s)):
            right_char=s[winend]
            if right_char not in char_freq:
                char_freq[right_char]=0
            char_freq[right_char]+=1
            if winend-winstart+1 > len(char_freq):
                left_char=s[winstart]
                char_freq[left_char]-=1
                if char_freq[left_char]==0:
                    del char_freq[left_char]
                winstart+=1
            maxlength=max(maxlength,winend-winstart+1)
        return maxlength
