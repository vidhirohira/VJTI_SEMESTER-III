import csv
from collections import defaultdict

count = 0

def merge(arr, left, mid, right):
    global count
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += (mid - i + 1)
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i - left]

def ms(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    ms(arr, left, mid)
    ms(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge_sort_and_count(arr):
    global count
    count = 0
    ms(arr, 0, len(arr) - 1)
    return count

file_path = 'testcase3.csv'
students_courses = []

with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_id = int(row['Student_ID'])
        courses = [int(row[f'Subject_{i}']) for i in range(1, 6)]
        students_courses.append((student_id, courses))

inversion_counts = []
for student_id, courses in students_courses:
    inversion_count = merge_sort_and_count(courses)
    inversion_counts.append(inversion_count)

inversion_groups = defaultdict(list)
for i, count in enumerate(inversion_counts):
    inversion_groups[count].append(i + 1)

for count, student_ids in sorted(inversion_groups.items()):
    print(f"Inversion Count {count}: Student IDs: {student_ids}")
