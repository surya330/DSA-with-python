def count_sort(A):
    count=[0]*(max(A)+1)
    n=len(A)
    temp=[0]*n
    for i in range(n):
        count[A[i]]+=1
    
    for i in range(1,len(count)):
        count[i]=count[i]+count[i-1]

    for i in range(n-1,-1,-1):
        count[A[i]]-=1
        temp[count[A[i]]]=A[i]

    for i in range(n):
        A[i]=temp[i]

A=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
count_sort(A)
print("The sorted array is:")
print(A)

