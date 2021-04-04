def shell_sort(A):
    n=len(A)
    gap=n//2
    while(gap>0):
        for i in range(gap,n):
            temp = A[i]
            j = i
            while(j>=gap and A[j-gap]>temp):
                A[j]=A[j-gap]
                j-=gap
            A[j] = temp
        gap //= 2
   
A=[23,29,15,19,31,7,9,5,2]
shell_sort(A)
print(A)
