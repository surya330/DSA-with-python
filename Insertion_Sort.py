def insertion_sort(A):
    v,j=0,0
    for i in range(1,len(A)):
        v=A[i]
        j=i
        while(A[j-1]>v and j>=1):
            A[j]=A[j-1]
            j-=1
        A[j]=v
    return A


array=[6,8,1,4,5,3,7,2]
print("The sorted list is:",end=" ")
print(insertion_sort(array))