#non-premptive

#process delcartioon
class Process :

    def __init__(self,id,at,bt):

        self.id = id
        self.at = at
        self.bt = bt
    
    def set_ct(self,ct):

        self.ct = ct
        self.tt = self.ct - self.at
        self.wt = self.tt - self.bt

    def __str__(self):
        return f'{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tt}\t{self.wt}'



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
l.sort(key=lambda x:(x.at,x.id))


#fcfs
final = []
ct = 0

for process in l:
    if ct < process.at :  #ct should be set properly
        ct = process.at
    ct+=process.bt
    
    process.set_ct(ct)
    final.append(process)  #append process to final


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
