#premptive

#process delcartioon
class Process :

    def __init__(self,id,at,bt):

        self.id = id
        self.at = at
        self.bt = bt
        self.rt = bt
    
    def set_ct(self,ct):

        self.ct = ct
        self.tt = self.ct - self.at
        self.wt = self.tt - self.bt

    def __str__(self):
        return f'{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tt}\t{self.wt}'

#queue implementation
class Queue:

    def __init__(self):
        self.q = []
    
    def push(self,x):
        self.q.append(x)
        self.update()
    
    def popout(self):
        self.q.pop(0)
    
    def front(self):
        if(len(self.q)):
            return self.q[0]
        else:
            return None
    
    def is_empty(self):
        return len(self.q)<=0
    
    def update(self):
        self.q.sort(key=lambda x:(-x.rt,x.at,x.id))
    

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


#lrjf

q=Queue()
final=[]

#intial step
time = l[0].at
while len(l) and l[0].at<=time:
        q.push(l[0])
        l.remove(l[0])



while not q.is_empty():

    cur = q.front()
    q.popout()

    if time<cur.at :
        time = cur.at
          
    time+=1
    cur.rt-=1

    if(cur.rt==0) : 
        cur.set_ct(time)
        print("Time set")
        final.append(cur)
    else:   
        q.push(cur)
        while len(l) and l[0].at<=time:
            q.push(l[0])
            l.remove(l[0])
        
     
    


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
