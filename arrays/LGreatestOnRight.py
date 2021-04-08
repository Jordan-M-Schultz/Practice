arr = [17,18,5,4,6,1]

ret = []
max = arr[len(arr) - 1]
save = -1
for i in range(len(arr) - 1, -1 , -1):
    save = arr[i]
    arr[i] = max
    if save > max:
        max = save
        
        
arr[len(arr) -1 ] = -1    
    