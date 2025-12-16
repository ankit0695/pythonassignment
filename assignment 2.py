# to check whether number is odd or even

num=int(input("enter number you want to check "))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")

# to calculate sum from 1 to 50 using for loop

sum=0
for i in range(1,51):
    sum=sum+i
print(sum)