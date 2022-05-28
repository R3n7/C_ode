#https://leetcode.com/problems/longest-repeating-character-replacement/submissions/
def characterReplacement(self, s: str, k: int) -> int:
    winstart=0
    maxlength=0
    char_fre={}
    for winend in range(len(s)):
        right_char=s[winend]
        if right_char not in char_fre:
            char_fre[right_char]=0
        char_fre[right_char]+=1
        if(winend-winstart+1-max(char_fre.values())>k):
            left_char=s[winstart]
            char_fre[left_char]-=1
            winstart+=1
        maxlength = max(maxlength,winend-winstart+1)

    return (maxlength)
