import numpy as np
              

def MST(G, n, r):
    totalWeight = 0
    sel = np.zeros(n) #included vertices list
    edges = 0
    sel[r] = 1  #start at r
    
    while edges < n-1:   #go until n-1 for MST
        key = float("inf")
        i = r
        j = r
        
        for u in range(n):
            if sel[u] == 1:   #if vertex u is included
                for v in range(n):
                    if sel[v] == 0 and G[u][v] < key: #if vertex v isnt included and the weight is less than the current key
                        key = G[u][v] #set the key and move there in the graph
                        i = u
                        j = v

        sel[j] = 1 #after looping through                  
        edges += 1 #increase number of edges
        totalWeight += key
        
    return totalWeight
        
    


f = open('graph.txt','r').readlines()

T = int(f.pop(0))

for i in range(T):
    numV = int(f.pop(0))
    G = np.zeros((numV,numV))
    X = [0]*numV
    Y = [0]*numV

    for j in range(numV):
        temp = f.pop(0)
        temp = temp.split()
        X[j] = int(temp[0])
        Y[j] = int(temp[1])

    

    for j in range(numV):
        for k in range(numV):
            G[j][k] = round(((X[j]-X[k])**2+(Y[j]-Y[k])**2)**0.5)


    print("Test case " + str(i) + ": MST weight " + str(int(MST(G,numV,0))))
    
    
