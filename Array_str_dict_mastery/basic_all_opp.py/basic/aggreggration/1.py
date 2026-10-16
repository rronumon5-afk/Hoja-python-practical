#1
a=[100,300,200]
print(sum(a))
#2
a=[10,20,30]
product=1
for num in a:
    product*=num
print(product)  

#3
a=[5,6,7,8,9]
print(max(a))

#4
a=[22,3,44,77,5,22,5,33]
print(min(a))  

#5
a=[10,20,30,40]
average=sum(a)/len(a)
print(average)

#6
a=[2,3,4,5,6,7,8,9,10]
even_sum=sum(num for num in a if num%2==0)
print(even_sum)

#7
a=[1,2,3,4,5,6]
odd_sum=sum(num for num in a if num%2!=0)
print(odd_sum)

#8
a=[1,23,1,33,8,6]
sum_even_indices=sum(a[i]for i in range(0,len(a),2))
print(sum_even_indices)

#9
a=[11,22,33,44,55]
difference=max(a)-min(a)
print(difference)

#10
a=[11,22,3,44,55]
sum_odd_indices=sum(a[i] for i  in range(1,len(a),2))
print(sum_odd_indices)
