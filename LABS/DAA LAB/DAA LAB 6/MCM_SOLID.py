from typing import List, Tuple


# Single Responsibility: Encapsulation of the Matrix Chain Multiplication logic
class MatrixChainMultiplier:
    def __init__(self, dimensions: List[int]):
        self.dimensions = dimensions
        self.dp = []

    def validate_dimensions(self, matrix_count: int) -> None:
        """
        Validates the input dimensions for matrix chain multiplication.
        Raises a ValueError if the input is invalid.
        """
        if matrix_count < 2:
            raise ValueError("There must be at least two matrices for multiplication.")
        if len(self.dimensions) != matrix_count + 1:
            raise ValueError("The dimensions array length must be N+1.")
        if any(dim <= 0 for dim in self.dimensions):
            raise ValueError("Matrix dimensions must be positive values.")

    def calculate_minimum_cost(self, matrix_count: int) -> int:
        """
        Calculates the minimum cost for matrix chain multiplication using dynamic programming.
        """
        self.dp = [[0 for _ in range(matrix_count)] for _ in range(matrix_count)]

        # Loop over chain lengths from 2 to matrix_count
        for chain_length in range(2, matrix_count + 1):
            for i in range(1, matrix_count - chain_length + 2):  # Start index
                j = i + chain_length - 1  # End index
                self.dp[i - 1][j - 1] = float('inf')

                for k in range(i, j):  # Partition point
                    cost = (self.dp[i - 1][k - 1] +
                            self.dp[k][j - 1] +
                            self.dimensions[i - 1] * self.dimensions[k] * self.dimensions[j])
                    self.dp[i - 1][j - 1] = min(self.dp[i - 1][j - 1], cost)

        return self.dp[0][matrix_count - 1]


# Single Responsibility: Test case processing
class TestCaseProcessor:
    def __init__(self, matrix_multiplier: MatrixChainMultiplier):
        self.matrix_multiplier = matrix_multiplier

    def run_test_case(self, matrix_count: int) -> Tuple[bool, str]:
        """
        Runs a single test case and returns a tuple of success status and message.
        """
        try:
            self.matrix_multiplier.validate_dimensions(matrix_count)
            result = self.matrix_multiplier.calculate_minimum_cost(matrix_count)
            return True, f"Minimum cost of multiplication: {result}"
        except ValueError as e:
            return False, f"Error: {e}"


# Single Responsibility: Handles test execution and output
class TestResultHandler:
    @staticmethod
    def print_result(dimensions: List[int], matrix_count: int, success: bool, message: str) -> None:
        """
        Prints the test case result.
        """
        status = "SUCCESS" if success else "FAILURE"
        print(f"[{status}] Test case with dimensions={dimensions}, matrix_count={matrix_count}: {message}")


# Dependency Inversion: Main test runner for handling multiple test cases
class TestRunner:
    def __init__(self, test_cases: List[Tuple[List[int], int]]):
        self.test_cases = test_cases

    def run_all_tests(self) -> None:
        result_handler = TestResultHandler()
        for dimensions, matrix_count in self.test_cases:
            multiplier = MatrixChainMultiplier(dimensions)
            processor = TestCaseProcessor(multiplier)
            success, message = processor.run_test_case(matrix_count)
            result_handler.print_result(dimensions, matrix_count, success, message)


# Main function to define test cases and execute tests
def main():
    test_cases = [
        # Valid test cases
        ([7, 5, 4, 6, 7, 8], 5),
        ([3, 7, 5, 10, 15], 4),
        ([2, 4, 5, 6, 8], 4),
        ([4, 8, 6, 7, 9], 4),
        ([7, 3, 6, 4, 8], 4),
        # Invalid test cases
        ([3, 7, 4, 7, 5], 5),
        ([2, 5, 6], 1),
        ([10, 20, 30], 2),
        ([10, 20], 1),
        ([10, -20, 10], 2),
        ([0, 20, 10], 2),
    ]

    runner = TestRunner(test_cases)
    runner.run_all_tests()


if __name__ == "__main__":
    main()
