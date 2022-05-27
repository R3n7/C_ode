winstart=0
s='cbbebi'
k=3
maxlength=0
char_fre={}
for winend in range(len(s)):
    right_char=s[winend]
    if right_char not in char_fre:
        char_fre[right_char]=0
    char_fre[right_char]+=1
    while len(char_fre)>k:
        left_char=s[winstart]
        char_fre[left_char]-=1
        if char_fre[left_char]==0:
            del char_fre[left_char]
        winstart+=1
    maxlength = max(winend-winstart+1,maxlength)
print(maxlength)
