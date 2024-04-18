#non-premptive

#process delcartioon
class Process :

    def __init__(self,id,at,bt):

        self.id = id
        self.at = at
        self.bt = bt
        self.wt = 0
    
    def set_ct(self,ct):

        self.ct = ct
        self.tt = self.ct - self.at
        self.wt = self.tt - self.bt

    def __str__(self):
        return f'{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tt}\t{self.wt}'


def rr(x):
     return (x.wt+x.bt)/x.bt

#queue implementation
class Queue:

    def __init__(self):
        self.q = []
    
    def push(self,x):
        self.q.append(x)
    
    def popout(self):
        self.q.pop(0)
    
    def front(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q)<=0
    
    def update(self):
        self.q.sort(key=lambda x:(-rr(x),x.at,x.id))
        

    
#input   
n = int(input("No of proccess:"))
l = []

for i in range(n):
    print(f"Process {i+1}")
    at = int(input("Arrival Time:"))
    bt = int(input("Burst Time:"))
    l.append(Process(i+1,at,bt))
    print()

#sort based on arrival
l.sort(key=lambda x:x.at)




#hrrn

q=Queue()
final=[]

#intial step
time = l[0].at
while len(l) and l[0].at<=time:
        q.push(l[0])
        l.remove(l[0])
q.update()


#hrrn
while not q.is_empty():

    cur = q.front()
    q.popout()

    if time<cur.at :
        time = cur.at
    
    time += cur.bt
    cur.set_ct(time)
    final.append(cur)

    while len(l) and l[0].at<=time:
        q.push(l[0])
        l.remove(l[0])
    
    #re-updation
    for process in q.q:
        process.wt = time - process.at
    q.update()
    

    
    


final.sort(key=lambda x:x.id)
print('ID\tAT\tBT\tCT\tTAT\tWT')
for process in final :
    print(process)


#averages
avg_ct = 0
avg_tt = 0
avg_wt = 0

for i in final:
    avg_ct+=i.ct
    avg_tt+=i.tt
    avg_wt+=i.wt

print(f'Average CT : {avg_ct/n}')
print(f'Average TT : {avg_tt/n}')
print(f'Average WT : {avg_wt/n}')

     
