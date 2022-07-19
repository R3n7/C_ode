def searchpair(list1,targetsum,trip):
    left,right =0,len(list1)-1
    currentsum=0
    while (left<right):
        currentsum=list1[left]+list1[right]
        #print(currentsum,list1[left],list1[right])

        if currentsum>targetsum:
            right-=1
        elif currentsum<targetsum:
            left+=1
        elif currentsum == targetsum :
            x = [-targetsum,list1[left],list1[right]]
            x.sort()
            if len(set(x)) == 3 and x not in trip:
                trip.append([-targetsum,list1[left],list1[right]])
            left+=1
            right-=1
    #print(-1)
list1 = [-5, 2, -1, -2, 3]
list1.sort()
prev = 'q'
trip = [ ]
for i in list1:
    if prev != i:
        prev = i
        targetsum = -i
        #print(i)
        searchpair(list1,targetsum,trip)
print(trip)
