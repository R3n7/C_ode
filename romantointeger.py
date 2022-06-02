#https://leetcode.com/problems/roman-to-integer/submissions/
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,' ':0}
        count=0
        c1 =0
        str3=' '
        for i in s:
            str3 +=i
            #print(str3)
            if hashmap[str3[-2]]<hashmap[str3[-1]]:
                #print(str3[-2],str3[-1])
                c1 += 2*hashmap[str3[-2]]
                #print(str3,count,c1,type(hashmap[str3[-2]]))
            
            count+=hashmap[i]
            #print(str3,count)
        return count-c1
