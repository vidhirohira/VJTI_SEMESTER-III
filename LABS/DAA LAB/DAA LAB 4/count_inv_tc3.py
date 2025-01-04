def count_inversions_brute_force(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def count_inversions_divide_and_conquer(arr):
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
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    inversions = 0
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            inversions += (mid - i + 1 - left)
            j += 1
        k += 1
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
    [1, 2, 3, 4], [1, 1, 5, 2], [7, 6, 4, 1], [6, 2, 8, 7], [2, 3, 8, 4], [1, 5, 5, 4], [4, 8, 5, 3], [8, 1, 9, 6],
    [1, 4, 1, 1], [1, 3, 5, 3], [8, 7, 3, 8], [1, 4, 4, 8], [1, 2, 5, 4], [1, 7, 1, 6], [6, 5, 7, 6], [9, 7, 5, 5],
    [1, 8, 2, 2], [1, 3, 7, 8], [2, 3, 8, 2], [8, 6, 7, 4], [9, 6, 9, 9], [1, 5, 8, 9], [5, 2, 3, 8], [9, 3, 1, 4],
    [1, 5, 2, 9], [1, 3, 1, 1], [5, 6, 7, 9], [8, 5, 1, 1], [2, 2, 2, 3], [1, 6, 9, 4], [7, 5, 1, 4], [6, 2, 1, 4],
    [1, 2, 8, 9], [1, 6, 3, 7], [6, 6, 5, 9], [8, 5, 9, 5], [1, 6, 2, 6], [1, 4, 6, 9], [3, 7, 1, 4], [4, 1, 1, 6],
    [1, 5, 6, 6], [1, 5, 4, 2], [4, 2, 5, 3], [2, 2, 4, 1], [1, 7, 9, 9], [1, 4, 7, 8], [6, 7, 3, 3], [5, 4, 5, 4],
    [1, 4, 6, 9], [1, 7, 8, 2], [5, 7, 5, 3], [9, 8, 2, 2], [1, 8, 3, 6], [1, 8, 7, 7], [4, 6, 6, 9], [2, 1, 1, 2],
    [1, 6, 6, 2], [1, 7, 9, 8], [6, 1, 4, 1], [4, 5, 7, 8], [1, 1, 3, 6], [1, 3, 4, 5], [6, 3, 3, 5], [5, 4, 1, 9],
    [1, 2, 7, 4], [1, 7, 2, 8], [5, 1, 2, 1], [8, 9, 5, 4], [1, 1, 9, 5], [1, 4, 9, 4], [8, 1, 8, 5], [6, 2, 1, 6],
    [1, 4, 1, 7], [1, 5, 2, 5], [9, 3, 9, 1], [2, 1, 7, 5], [1, 4, 8, 5], [4, 4, 9, 8], [8, 2, 3, 8], [4, 5, 5, 1],
    [1, 9, 5, 5], [8, 5, 6, 3], [3, 2, 6, 3], [5, 1, 7, 5], [6, 5, 7, 8], [1, 7, 3, 4], [2, 1, 4, 5], [2, 6, 3, 8],
    [1, 3, 8, 2], [3, 3, 5, 6], [3, 7, 5, 1], [1, 5, 5, 3], [9, 1, 9, 7], [1, 2, 5, 5], [4, 6, 7, 6], [6, 8, 1, 1],
    [1, 2, 6, 9], [1, 4, 4, 8], [2, 3, 3, 9], [1, 2, 7, 3]
]

brute_force_inversion_counts = [count_inversions_brute_force(sublist) for sublist in students_random_numbers]
divide_and_conquer_inversion_counts = [count_inversions_divide_and_conquer(sublist[:]) for sublist in students_random_numbers]

total_inversion_count_brute_force = sum(brute_force_inversion_counts)
total_inversion_count_divide_and_conquer = sum(divide_and_conquer_inversion_counts)

def categorize_inversion_counts(inversion_counts):
    categories = {}
    for index, count in enumerate(inversion_counts):
        if count not in categories:
            categories[count] = []
        categories[count].append(index + 1)
    return categories

brute_force_categories = categorize_inversion_counts(brute_force_inversion_counts)
divide_and_conquer_categories = categorize_inversion_counts(divide_and_conquer_inversion_counts)

print("Total inversion count (Brute Force) across all students:", total_inversion_count_brute_force)
print("Total inversion count (Divide and Conquer) across all students:", total_inversion_count_divide_and_conquer)

print("\nCategorized Inversion Counts (Brute Force):")
for count, students in sorted(brute_force_categories.items()):
    print(f"Inversion Count {count}: Students {students}")

print("\nCategorized Inversion Counts (Divide and Conquer):")
for count, students in sorted(divide_and_conquer_categories.items()):
    print(f"Inversion Count {count}: Students {students}")
