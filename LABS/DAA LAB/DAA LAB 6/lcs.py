import pandas as pd
import re

# Define the LCS function
def lcs(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_sequence = []
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_sequence.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_sequence))

# Function to check the validity of the grades
def validate_grades(grades):
    if len(grades) != 40:
        raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")
    
    if any(char.isdigit() for char in grades):
        raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")
    
    if not all(re.match(r"[A-F]{2}", grades[i:i+2]) for i in range(0, len(grades), 2)):
        raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")

# Handle positive test cases
print("Positive Test Cases:")
for i in range(1, 5):
    file_path = f"positive_test_case_{i}.csv"
    df = pd.read_csv(file_path)

    # Extract the grades column as a list
    grades_list = df["Grades"].tolist()

    # Initialize LCS as the first student's grades
    overall_lcs = grades_list[0]
    for i in range(1, len(grades_list)):
        try:
            # Validate each student's grade sequence
            validate_grades(grades_list[i])
            # Calculate LCS only if the grades are valid
            overall_lcs = lcs(overall_lcs, grades_list[i])
        except ValueError as e:
            print(f"Error for student {df.iloc[i]['Student ID']}: {e}")

    print(f"Longest Common Subsequence of Grades for All Students in Test Case {i}:", overall_lcs)

# Handle negative test cases
print("\nNegative Test Cases:")
for i in range(1, 5):
    file_path = f"negative_test_case_{i}.csv"
    df = pd.read_csv(file_path)

    # Extract the grades column as a list
    grades_list = df["Grades"].tolist()

    # Initialize LCS as the first student's grades
    overall_lcs = grades_list[0]
    error_found = False  # Flag to track if an error is found

    for i in range(1, len(grades_list)):
        try:
            # Validate each student's grade sequence
            validate_grades(grades_list[i])
            # Calculate LCS only if the grades are valid
            overall_lcs = lcs(overall_lcs, grades_list[i])
        except ValueError as e:
            print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
            error_found = True
            break  # No need to process further if there's an error

    if not error_found:
        print(f"Longest Common Subsequence of Grades for All Students in Test Case {i}:", overall_lcs)
    else:
        print(f"Error detected in Test Case {i}. Skipping LCS calculation.")
