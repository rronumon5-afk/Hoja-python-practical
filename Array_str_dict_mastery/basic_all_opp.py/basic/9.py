num=[1,2,3,2,4,2,5,2]
old,new=2,1000
num=[new if x==old else x for x in num]
print(num)