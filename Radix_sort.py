def radix_sort(A):
    max_value=max(A)
    pos=1
    while(max_value//pos>0):
        count_sort(A,pos)
        pos*=10

def count_sort(A,pos):
    count=[0]*10
    n=len(A)
    temp=[0]*n
    for i in range(n):
        count[(A[i]//pos)%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        count[(A[i]//pos)%10]-=1
        temp[count[(A[i]//pos)%10]]=A[i]
    for i in range(n):
        A[i]=temp[i]

A=[432,8,530,90,88,231,11,45,677,199]
radix_sort(A)
print(A)

