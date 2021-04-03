def selectionsort(A):
    min=0
    for i in range(len(A)-1):
        min=i
        for j in range(i+1,len(A)):
            if(A[j]<A[min]):
                min=j
        A[min],A[i]=A[i],A[min]
    return A

array=[6,8,1,4,5,3,7,2]
print("The sorted list is:",end=" ")
print(selectionsort(array))

