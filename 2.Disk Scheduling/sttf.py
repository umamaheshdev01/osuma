def near_sort(a,k):
    
    fine=[k]
    prev=k
    
    while len(a):
        fine.append(min(a,key=lambda x:abs(x-prev)))
        prev=fine[-1]
        a.remove(prev)
    
    return fine


intial = int(input("Intial position:"))
order = list(map(int,input("Enter Order of Request:").split()))


order=near_sort(order,intial)
final=[]

prev=intial
overhead=0

while len(order):
    x=order[0]
    order.pop(0)

    overhead+=abs(x-prev)
    prev=x
    final.append(x)


print("Seek order:")
print("-->".join([str(i) for i in final]))
print("Total Overhead: ",end="")
print(overhead)


