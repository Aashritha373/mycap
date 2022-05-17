FIBONACCI SERIES
n=int(input("Number of elements in fibonacci series"))
a=0
b=1 
sum=0
print(a)
print(b)
for i in range(2,n):
    sum = a+b 
    a=b
    b=sum
    print(sum)    
