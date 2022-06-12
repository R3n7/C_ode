#https://leetcode.com/problems/maximum-erasure-value/submissions/
#My original code
winstart=0
max_length =0
char_freq = {}
for i in range(len(nums)):
    if nums[i] not in char_freq:
        char_freq[nums[i]]=0
    char_freq[nums[i]]+=1
    #print(char_freq)
    if len(char_freq) != sum(char_freq.values()):
        char_freq[nums[winstart]]-=1
        if char_freq[nums[winstart]]==0:
            del char_freq[nums[winstart]]
        winstart+=1
    max_length = max(max_length,sum(char_freq.keys()))
return max_length

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter=defaultdict(int) # track count of  elements in the window
        res=i=tot=0
		
        for j in range(len(nums)):
            x=nums[j]   
            tot+=x
            counter[x]+=1
            # adjust the left bound of sliding window until you get all unique elements
            while i < j and counter[x]>1: 
                counter[nums[i]]-=1
                tot-=nums[i]
                i+=1
            
            res=max(res, tot)            
        return res
