AREA OF CIRCLE
r=float(input("Enter the radius of the circle : "))
area = 3.14*r**2
print("The area of the circle with radius",r,"is:",area)

EXTENSION OF FILE
f=input("Input the Filename:")
f_e = f.split(".")
print("The extension of the file is : "+repr(f_e[-1]))

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
    
