def max_sum_sub_array(array: list):
    """
    1. brute force
    2. Kadane's Algorithm
    -> local_maximum[i] = max(a[i], a[i]+local_maximum[i-1]
    """
    #max_sub_array = float('-inf')
    #for i in range(0, len(array)):
    #    for j in range(i, len(array)):
    #        max_sub_array = max(max_sub_array, sum(array[i:j+1]))
    #return max_sub_array

    local_min = 0
    global_min = float('-inf')
    for i in range(len(array)):
        local_min = max(array[i], array[i]+local_min)
        if local_min > global_min:
            global_min = local_min
    return global_min

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum_sub = max_sum_sub_array(array)
print(max_sum_sub)
