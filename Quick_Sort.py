def Quick_sort(A,low,high):
    if(low<high):
        pivot=partition(A,low,high)
        Quick_sort(A,low,pivot-1)
        Quick_sort(A,pivot+1,high)

def partition(A,low,high):
    pivot_item=A[low]
    left=low
    right=high
    while(left<right):
        while(A[left]<=pivot_item):
            left+=1
        while(A[right]>pivot_item):
            right-=1
        if(left<right):
            A[left],A[right]=A[right],A[left]
    
    A[low]=A[right]
    A[right]=pivot_item
    return right

A=[6,8,1,4,5,3,7,2]
low=0
high=len(A)-1
Quick_sort(A,low,high)
print(A)
