# Brute force method to count the number of inversions in a list
def count_inversions_brute_force(arr):
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return "Error: Array contains non-integer values, inversion count can't be performed."
    
    inversions = 0
    n = len(arr)
    
    # Compare each pair (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
                
    return inversions

# Divide and conquer (merge sort) method to count the number of inversions in a list
def count_inversions_divide_and_conquer(arr):
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return "Error: Array contains non-integer values, inversion count can't be performed."
    
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inversions = merge_sort(arr, left, mid)
    inversions += merge_sort(arr, mid + 1, right)
    inversions += merge_and_count(arr, left, mid, right)
    
    return inversions

def merge_and_count(arr, left, mid, right):
    # Left and right subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    inversions = 0
    
    # Merge while counting inversions
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            inversions += (mid - i + 1 - left)  # Count inversions
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1
    
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1
        
    return inversions


students_random_numbers = [
    [1, 2, 3, 4], [False, 1, 5, 2], [-7, 6, 4, 1], [6, 2, 8, 7], [2, 3, 8, 4], [5, 5, 5, 4], [4, True, 5, 3], [8, 1, 9, 6],
    [3, 4, 1, 1], [8, 3, 5, 3], [8, 7, 3, 8], [1, 4, 4, 8], [1, 2, 5, 4], [5, 7, 1, 6], [6, 5, 7, 6], [9, 7, 5, 5],
    [5, 8, 2, 2], [1, 3, 7, 8], [2, 3, -8, 2], [8, 6, 7, 4], [False, 6, 9, 9], [6, 5, 8, 9], [5, 2, 3, 8], [9, 3, 1, 4],
    [4, 5, 2, 9], [7, 3, 1, 1], [5, 6, 7, 9], [8, 5, 1, 1], [2, 2, 2, 3], [9, 6, 9, 4], [7, 5, 1, 4], [6, 2, 1, 4],
    [6, 2, 8, 9], [8, 6, 6, 7], [6, 6, 5, 9], [8, 5, 9, 5], [1, 6, 2, 6], [1, 4, True, 9], [3, 7, 1, 4], [4, 1, 1, 6],
    [5, 5, 6, 6], [6, 5, 4, 2], [4, 2, 5, 3], [-2, 2, False, 1], [2, 7, 9, 9], [6, 4, 7, 8], [6, 7, 3, 3], [5, 4, 5, 4],
    [3, 4, 6, 9], [2, False, 8, 2], [5, 7, 5, 3], [9, 8, 2, 2], [9, 8, 3, 6], [3, 8, 7, 7], [4, 6, 6, 9], [2, 1, 1, 2],
    [3, 6, 6, 2], [4, 7, 9, 8], [6, 1, 4, 1], [4, 5, 7, 8], [1, 1, 3, 6], [9, 3, 4, 5], [6, 3, 3, 5], [5, 4, 1, 9],
    [5, 2, 7, 4], [4, 7, 2, 8], [5, 1, 2, 1], [8, 9, 5, 4], [3, 1, 9, 5], [9, 4, 9, 4], [8, 1, 8, 5], [6, 2, 1, 6],
    [3, 4, 1, 7], [8, 5, 2, 5], [9, 3, 9, 1], [2, 9, 7, 5], [5, 4, 8, 5], [4, True, 9, 8], [8, 2, 3, 8], [4, 5, 5, 1],
    [4, True, 5, 5], [8, 5, 6, 3], [3, 2, True, 3], [5, 1, 7, 5], [6, 5, 7, 8], [3, 7, 3, 4], [2, 1, 4, 5], [2, 6, 3, 8],
    [4, 3, 8, 2], [3, 3, 5, 6], [3, 7, 5, 1], [1, 5, 5, 3], [9, 1, 9, 7], [1, 2, 5, 5], [4, 6, 7, 6], [6, 8, 1, 1],
    [2, 2, 6, 9], [3, 4, 4, 8], [2, 3, 3, 9], [3, 2, 7, 3]
]

valid_inversion_counts = []
negative_inversion_counts = []
error_messages = []

# Process each sublist for inversion counts
for index, sublist in enumerate(students_random_numbers):
    if any(isinstance(x, bool) for x in sublist):  # Check if any element is a boolean
        error_messages.append((index + 1, "ERROR: Inversion count can't be found due to the presence of boolean values."))
    elif all(isinstance(x, int) for x in sublist):  # Check if all elements are integers
        if all(x < 0 for x in sublist):  # Check if all elements are negative
            negative_inversion_counts.append((index + 1, "ERROR: Inversion count can't be found since course code can't be negative."))
        else:
            brute_force_count = count_inversions_brute_force(sublist)
            divide_and_conquer_count = count_inversions_divide_and_conquer(sublist[:])
            valid_inversion_counts.append((index + 1, brute_force_count, divide_and_conquer_count))
    else:
        error_messages.append((index + 1, "Error: Array contains letters instead of integer values, inversion count can't be performed."))

# Display results for valid inversion counts
print("\nCategorized Inversion Counts (Valid Entries):")
for student_index, bf_count, dc_count in valid_inversion_counts:
    print(f"Student {student_index}: Brute Force Inversion Count = {bf_count}, Divide and Conquer Inversion Count = {dc_count}")

# Display results for negative integer entries
print("\nNegative Integer Entries:")
for student_index, message in negative_inversion_counts:
    print(f"Student {student_index}: {message}")

# Display error messages for invalid entries
print("\nError Messages for Invalid Entries:")
for student_index, error in error_messages:
    print(f"Student {student_index}: {error}")
