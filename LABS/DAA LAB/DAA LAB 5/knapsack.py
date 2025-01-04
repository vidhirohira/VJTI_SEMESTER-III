import random

# Class to represent an item in the knapsack
class Item:
    def __init__(self, weight, value, shelf_life):
        if weight <= 0:
            raise ValueError(f"Invalid weight: {weight}. Weight of an item cannot be zero or negative.")
        if value < 0:
            raise ValueError(f"Invalid value: {value}. Value of an item cannot be negative.")
        if shelf_life <= 0:
            raise ValueError(f"Invalid shelf life: {shelf_life}. Shelf life must be greater than zero.")
        self.weight = weight
        self.value = value
        self.shelf_life = shelf_life

    # Utility function to calculate the value to weight ratio
    def value_weight_ratio(self):
        return self.value / self.weight

    # Utility function to combine shelf life and value-weight ratio in comparison
    def priority(self):
        return (self.value_weight_ratio(), -self.shelf_life)  # Higher value-weight, lower shelf life prioritized

# Function to implement the fractional knapsack problem
def fractional_knapsack(capacity, items):
    if capacity <= 0:
        raise ValueError("Capacity of the knapsack must be greater than zero.")
    if len(items) == 0:
        raise ValueError("Item list cannot be empty.")
    
    # Sort items by priority: value-weight ratio (desc) and shelf life (asc)
    items.sort(key=lambda x: x.priority(), reverse=True)
    
    total_value = 0  # Total value accumulated
    current_weight = 0  # Current weight of the knapsack
    
    for item in items:
        if current_weight + item.weight <= capacity:
            # Take the whole item
            current_weight += item.weight
            total_value += item.value
        else:
            # Take fraction of the item
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / item.weight
            total_value += item.value * fraction
            break  # Knapsack is full
    
    return total_value

# Test case runner with error handling
def run_test_case(items, capacity):
    try:
        # Print the items with their weights, values, and shelf lives
        print("\nItems (Weight, Value, Shelf Life):")
        for idx, item in enumerate(items):
            print(f"Item {idx + 1}: Weight = {item.weight}, Value = {item.value}, Shelf Life = {item.shelf_life}")

        # Calculate and print the total knapsack value
        result = fractional_knapsack(capacity, items)
        print(f"Knapsack Value for {len(items)} items: {result:.2f}\n")
    
    except ValueError as e:
        print(f"Error: {e}")

# Create a list of 100 items with random weights, values, and shelf lives
items_100 = [Item(random.randint(1, 50), random.randint(10, 500), random.randint(1, 30)) for _ in range(100)]

# Test case with knapsack capacity of 200 tones
capacity = 300

# Running the test case
run_test_case(items_100, capacity)


# Positive Test Cases
print("\nPositive Test Cases")

items_1 = [Item(10, 60, 5), Item(20, 100, 10), Item(30, 120, 3)]
run_test_case(items_1, 200)  # Expected: Can take 100% of first two items (160) + 2/3 of the last (80)

items_2 = [Item(5, 50, 1), Item(10, 60, 2), Item(15, 90, 4)]
run_test_case(items_2, 200)  # Expected: Can take first item + second item (total 110) + part of third

items_3 = [Item(5, 30, 8), Item(10, 20, 6), Item(20, 100, 2), Item(15, 60, 5)]
run_test_case(items_3, 200)  # Expected: Highest ratio items should be fully taken

items_4 = [Item(10, 60, 3), Item(10, 100, 2), Item(10, 120, 1)]
run_test_case(items_4, 200)  # Expected: Take the first two items fully and part of the third.

items_5 = [Item(5, 50, 3), Item(8, 60, 1), Item(12, 90, 2)]
run_test_case(items_5, 200)  # Expected: Take first fully and part of second.


# Negative Test Cases with proper error handling
print("\nNegative Test Cases")

# Empty item list
items_6 = []
run_test_case(items_6, 200)  # Expected: Error for empty item list

# Knapsack capacity is zero
items_7 = [Item(5, 30, 3), Item(10, 50, 5)]
run_test_case(items_7, 0)  # Expected: Error for zero capacity

# Items with 0 value (valid but results in 0 knapsack value)
items_8 = [Item(10, 0, 5), Item(20, 0, 3)]
run_test_case(items_8, 200)  # Expected: Should work with zero-value items, total value = 0.

# Item heavier than the knapsack
items_9 = [Item(300, 1000, 5)]
run_test_case(items_9, 200)  # Expected: Take fraction of the item (200/300)

# Items with zero or negative weight, value, or shelf life
try:
    items_10 = [Item(0, 100, 5)]  # Item with zero weight
except ValueError as e:
    print(f"Error: {e}")  # Expected: Error for zero weight

try:
    items_11 = [Item(-10, 100, 5)]  # Item with negative weight
except ValueError as e:
    print(f"Error: {e}")  # Expected: Error for negative weight

try:
    items_12 = [Item(10, -100, 5)]  # Item with negative value
except ValueError as e:
    print(f"Error: {e}")  # Expected: Error for negative value

try:
    items_13 = [Item(10, 100, 0)]  # Item with zero shelf life
except ValueError as e:
    print(f"Error: {e}")  # Expected: Error for zero shelf life
