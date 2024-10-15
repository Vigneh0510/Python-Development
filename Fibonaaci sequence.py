def fibonaaci_sequence(n):
    if n<=1 :
        return n
    return fibonaaci_sequence(n-1)+fibonaaci_sequence(n-2)
n=int(input())
for i in range(n):
    print(fibonaaci_sequence(i),end=" ")