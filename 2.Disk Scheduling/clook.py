def look_sort(a,k):
    
    first = sorted([i for i in a if i>k])
    last = sorted([i for i in a if i<k])

    return first+last


intial = int(input("Intial position:"))
order = list(map(int,input("Enter Order of Request:").split()))

start=0
end=199

order=look_sort(order,intial)
final=[intial]

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


