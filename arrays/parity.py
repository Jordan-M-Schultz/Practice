def sortArrayByParity(A):
    if len(A) == 1 : 
        return A
    
    temp = 0
    for i in range(len(A)) : 
        if A[i] % 2 == 1 : #odd
            for j in range(i+1,len(A)) : 
                if A[j] % 2 == 0 : 
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
                    break
    return A


print(sortArrayByParity([1,1,1,2]))