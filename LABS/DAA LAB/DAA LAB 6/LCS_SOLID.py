import pandas as pd
import re
from typing import List


# Validator for grade sequences
class GradeValidator:
    @staticmethod
    def validate(grades: str) -> None:
        if len(grades) != 40:
            raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")

        if any(char.isdigit() for char in grades):
            raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")

        if not all(re.match(r"[A-F]{2}", grades[i:i + 2]) for i in range(0, len(grades), 2)):
            raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")


# Abstraction for LCS calculation
class LCSCalculator:
    @staticmethod 
    def calculate_lcs(str1: str, str2: str) -> str:
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


# File processor for handling test cases
class TestCaseProcessor:
    def __init__(self, lcs_calculator: LCSCalculator, grade_validator: GradeValidator):
        self.lcs_calculator = lcs_calculator
        self.grade_validator = grade_validator

    def process_test_case(self, file_path: str) -> str:
        df = pd.read_csv(file_path)
        grades_list = df["Grades"].tolist()

        overall_lcs = grades_list[0]
        for i in range(1, len(grades_list)):
            try:
                self.grade_validator.validate(grades_list[i])
                overall_lcs = self.lcs_calculator.calculate_lcs(overall_lcs, grades_list[i])
            except ValueError as e:
                print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
                return "Error detected. Skipping LCS calculation."

        return f"Longest Common Subsequence of Grades: {overall_lcs}"


# Main processing of positive and negative test cases
def main():
    lcs_calculator = LCSCalculator()
    grade_validator = GradeValidator()
    processor = TestCaseProcessor(lcs_calculator, grade_validator)

    print("Positive Test Cases:")
    for i in range(1, 5):
        file_path = f"positive_test_case_{i}.csv"
        result = processor.process_test_case(file_path)
        print(f"Test Case {i}: {result}")

    print("\nNegative Test Cases:")
    for i in range(1, 5):
        file_path = f"negative_test_case_{i}.csv"
        result = processor.process_test_case(file_path)
        print(f"Test Case {i}: {result}")


if __name__ == "__main__":
    main()
