# Program to reverse an array.

# function to reverse the give the array 
# from start to end
def reverse_array(A):
    start = 0
    end = len(A) - 1
    while(start < end):
        A[start], A[end] = A[end], A[start]
        start+=1
        end-=1
    return A

# Driver Function
A = [1,2,3,4,5,6,7]
reverse_array(A)
print("The reversed list is",A)
