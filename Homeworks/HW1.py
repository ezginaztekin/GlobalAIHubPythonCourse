oddnumbers=[1,3,5,7,9,11,13,15,17,19,21]
evennumbers=[0,2,4,6,8,10,12,14,16,18,20]

list= evennumbers+oddnumbers
list.sort()
print(list)

newlist=[i*2 for i in list]
print(newlist)

for x in newlist:
    print(type(x))
