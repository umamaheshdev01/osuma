class WaitForGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = set()
        self.graph[a].add(b)

    def detect_deadlock(self):
        visited = set()
        in_progress = set()

        def dfs(node):
            if node in in_progress:
                return True 
            if node in visited:
                return False  

            visited.add(node)
            in_progress.add(node)

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if dfs(neighbor):
                        return True

            in_progress.remove(node)
            return False

        for node in self.graph.keys():
            if node not in visited:
                if dfs(node):
                    return True  

        return False  


graph = WaitForGraph()

print('Enter the allocation (u-->v),-1 to stop')

while True:
    k=input()
    if '-1' in k : break

    u,v = k.split()
    graph.add_edge(u,v)

if graph.detect_deadlock():
    print('Deadlock Detected')
else:
    print('No Deadlock')
