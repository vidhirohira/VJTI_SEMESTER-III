import csv
from collections import defaultdict

# Function to count inversions in an array
def count_inversions(arr):
    count = 0
    n = len(arr)
    
    # Using a simple nested loop to count inversions
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

# Read data from CSV file
file_path = 'students_courses.csv'
students_courses = []

with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_id = int(row['Student_ID'])
        courses = list(map(int, row['Courses'].split(', ')))
        students_courses.append((student_id, courses))

# Calculate count inversions for each student and store them in a list
inversion_counts = []
for student_id, courses in students_courses:
    inversion_count = count_inversions(courses)
    inversion_counts.append(inversion_count)

# Group students by their inversion counts
inversion_groups = defaultdict(list)
for i, count in enumerate(inversion_counts):
    inversion_groups[count].append(i + 1)  # Store 1-based student ID

# Return the grouped results
grouped_students = dict(inversion_groups)
# Print the grouped students by inversion count in ascending order
for count, student_ids in sorted(grouped_students.items()):
    print(f"Inversion Count {count}: Student IDs: {student_ids}")




