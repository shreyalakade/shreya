n=int(input("enter a number:"))

a=0

b=1

c=3

print(a)

print(b)

for i in range(1,n+1):

    while n>=c:

        d=a+b

        a,b=b,d

        if d<=n:

            print(d)