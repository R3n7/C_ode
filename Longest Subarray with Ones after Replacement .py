winstart=0
s= [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k=3
maxlength=0
char_fre={}
char_fre[1]=0
for winend in range(len(s)):
    right_char=s[winend]
    if right_char not in char_fre:
        char_fre[right_char]=0
    char_fre[right_char]+=1
    #print(char_fre)
    if(sum(char_fre.values())-char_fre[1]>k):
        left_char=s[winstart]
        char_fre[left_char]-=1
        winstart+=1
        if char_fre[left_char]==0:
            del char_fre[left_char]
    maxlength = max(maxlength,winend-winstart+1)
        
print(maxlength)
