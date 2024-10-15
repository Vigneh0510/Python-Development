n=int(input())
a=bin(n).count('1')
print(a)

sum=0
n=int(input())
while n>0:
    rem=n%2
    sum+=rem
    n=int(n/2)
print(sum)
    

