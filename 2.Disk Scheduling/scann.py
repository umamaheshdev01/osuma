def scan_sort(a,k,end):
    
    first = sorted([i for i in a if i>k])
    middle = [end if end not in first else None]
    last = sorted([i for i in a if i<k],key=lambda x:-x)

    return first+middle+last


intial = int(input("Intial position:"))
order = list(map(int,input("Enter Order of Request:").split()))

start=0
end=199

order=scan_sort(order,intial,end)
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


