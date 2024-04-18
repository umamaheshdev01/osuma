def scan_sort(a,k,end,start):
    
    first = sorted([i for i in a if i>k])
    last = sorted([i for i in a if i<k])
    middle = [end if end not in first else None]+[start if start not in last else None]

    return first+middle+last


intial = int(input("Intial position:"))
order = list(map(int,input("Enter Order of Request:").split()))

start=0
end=199

order=scan_sort(order,intial,end,start)
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