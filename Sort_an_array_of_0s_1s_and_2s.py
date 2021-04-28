# Program to sort an array with elements 
# 0's, 1's and 2's without using any sorting 
# technique and extra space.

# Function for sorting the elements

def sort_arr(A):
    low = 0
    high = len(A) - 1
    mid = 0

    while(mid <= high):
        if A[mid] == 0:
            A[low], A[mid] = A[mid], A[low]
            low += 1
            mid += 1
        elif A[mid] == 1:
            mid += 1
        else:
            A[high], A[mid] = A[mid], A[high]
            high -= 1
    return A

#Driver function
A=[0,1,0,2,1,0,2]
print("Here is the sorted array",sort_arr(A))
