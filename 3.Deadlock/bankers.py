class Process:

    def __init__(self,id,A_alloc,B_alloc,C_alloc,A_max,B_max,C_max):
        
         self.id = id
         
         self.A_alloc = A_alloc
         self.B_alloc = B_alloc
         self.C_alloc = C_alloc

         self.A_max = A_max
         self.B_max = B_max
         self.C_max = C_max

         self.A_need = A_max - A_alloc
         self.B_need = B_max - B_alloc
         self.C_need = C_max - C_alloc


class System :
     
     def __init__(self,A,B,C):
          self.A = A
          self.B = B
          self.C = C


#input
n = int(input("No of Process:"))
l=[]

for i in range(n):
     
     print(f"Process {i+1}")
     id=i+1

     a,b,c = map(int,input("Enter the allocated resources (A,B,C):").split())
     A,B,C = map(int,input("Enter the max resources(A,B,C):").split())

     l.append(Process(id,a,b,c,A,B,C))
     print()


a,b,c = map(int,input("Enter the available Resources(A,B,C):").split())
sys = System(a,b,c)



#bankers algo
final = []

while len(l):
     
     process = l[0]
     l.remove(process)

     if (process.A_need,process.B_need,process.C_need) <= (sys.A,sys.B,sys.C):
          final.append(process)
          sys.A+=process.A_alloc
          sys.B+=process.B_alloc
          sys.C+=process.C_alloc
     else:
          l.append(process)


#Output
print()
print("The sequence of the process are:")
print("--->".join([str(i.id) for i in final]))
          

