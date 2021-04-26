#Program to find maximum continuos subarray

#function to find maximum continuos subarray

def max_sub_array(a):
    max_so_far = a[0]
    max_ending_here = a[0]
    for i in range(1,len(a)):
        max_ending_here += a[i]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if(max_ending_here < 0):
            max_ending_here = 0
    return max_so_far

#Driver Function
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", max_sub_array(arr))
  