A=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
B=[4,5,6,7,8,9,10,11,27,28,30,31,33,36,39,45]

AXB=[]

for i in range(len(A)):
               for j in range(len(B)):
                   AXB.append((A[i],B[j]))

print(AXB)
                   
