import numpy as np

A = np.zeros((9,9))

for i in range (A.shape[0]):
    for j in range (A.shape[1]):
        
        if i % 2 == 1:
            A[i][j] = 1
        
        if j % 2 == 0:
            A[i][j] = 0
            
print(A)
#    
#        

        
        
      
        
        
    


#print(a)
#b = np.zeros(9)
#print(b)


