def bubblesort(A):
    swapped=1
    for p in range(len(A)-1,-1,-1):
        if(swapped):
            swapped=0
            for i in range(p):
                if(A[i]>A[i+1]):
                    A[i],A[i+1]=A[i+1],A[i]
                    swapped=1
    return A

array=[1,2,3,4,5,6,7]
print("The sorted array is:",end=" ")
print(bubblesort(array))
