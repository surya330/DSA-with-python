# Program to find the maximum and minimum 
# element in the array.

# Function to return the max and min 
# elements of the given array.
def Find_minmax(A, low, high):

    if low == high:
        return A[low], A[high]
    
    elif high == low + 1:
        if A[low] > A[high]:
            return A[high], A[low]
        else:
            return A[low], A[high]
    
    else:
        mid = int((low+high)//2)
        arr_min1, arr_max1 = Find_minmax(A, low, mid)
        arr_min2, arr_max2 = Find_minmax(A, mid+1, high)
         
    return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))

# Driver Function
A = [100, 20, 40, 50, 10] 
low = 0
high = len(A) - 1
arr_min, arr_max=Find_minmax(A, low, high)
print("The minimum element is", arr_min)
print("The maximum element is", arr_max)



