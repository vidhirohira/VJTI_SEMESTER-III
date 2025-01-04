import numpy as np
import pandas as pd
df = pd.read_csv('employee_salary_information_with_id.csv')

# Extracting columns as numpy arrays
employee_id = df['Employee_ID'].values
basic_salary = df['Basic_Salary'].values
HRA = df['HRA'].values
other_allowances = df['Other_Allowances'].values
income_tax = df['Income_Tax'].values
employee_provident_fund = df['Employee_Provident_Fund'].values
professional_tax = df['Professional_Tax'].values

# Calculating Gross Salary
gross_salary = basic_salary + HRA + other_allowances

# Calculating Net Salary
net_salary = gross_salary - (income_tax + employee_provident_fund + professional_tax)

# Initialize variables for linear search
min_net_salary = net_salary[0]
max_net_salary = net_salary[0]
min_net_salary_employee_id = employee_id[0]
max_net_salary_employee_id = employee_id[0]

# Perform linear search
for i in range(1, len(net_salary)):
    if net_salary[i] < min_net_salary:
        min_net_salary = net_salary[i]
        min_net_salary_employee_id = employee_id[i]
    elif net_salary[i] > max_net_salary:
        max_net_salary = net_salary[i]
        max_net_salary_employee_id = employee_id[i]

# Printing the results
print("Using linear Search:")
print(f"Employee ID with minimum net salary: {min_net_salary_employee_id} with ₹{min_net_salary}")
print(f"Employee ID with maximum net salary: {max_net_salary_employee_id} with ₹{max_net_salary}")


def MinMaxSalary(net_salary, left, right):
    if left == right:
        return net_salary[left], net_salary[left]
    if right == left + 1:
        return min(net_salary[left], net_salary[right]), max(net_salary[left], net_salary[right])
    mid = left + (right - left) // 2
    min1, max1 = MinMaxSalary(net_salary, left, mid)
    min2, max2 = MinMaxSalary(net_salary, mid + 1, right)
    MinSalary = min(min1, min2)
    MaxSalary = max(max1, max2)
    return MinSalary, MaxSalary
    
print('Using divide and conquer approach:')
min, max = MinMaxSalary(net_salary,0,len(net_salary)-1)
print(f"Employee ID with minimum net salary: {min_net_salary_employee_id} with ₹{min}")
print(f"Employee ID with maximum net salary: {max_net_salary_employee_id} with ₹{max}")





test_files = [
    "employee_invalid_1.csv",
    "employee_invalid_2.csv",
    "employee_invalid_3.csv",
    "employee_valid_1.csv",
    "employee_valid_2.csv",
    "employee_valid_3.csv"
]

def run_test_cases():
    for file in test_files:
        try:
            print(f"Processing file: {file}")
            df_test = pd.read_csv(file)

            # Initialize an error flag
            error_flag = False

            # Check for negative values and empty cells
            for column in df_test.columns:
                if df_test[column].isnull().any():
                    print(f"Error: Empty cells found in column '{column}' in {file}")
                    error_flag = True
                if (df_test[column] < 0).any():
                    print(f"Error: Negative values found in column '{column}' in {file}")
                    error_flag = True

            # Skip salary calculations if there are errors
            if error_flag:
                print("Skipping salary calculations due to data errors.\n")
                continue

            employee_id = df_test['Employee_ID'].values
            basic_salary = df_test['Basic_Salary'].values
            HRA = df_test['HRA'].values
            other_allowances = df_test['Other_Allowances'].values
            employee_provident_fund = df_test['Employee_Provident_Fund'].values
            income_tax = df_test['Income_Tax'].values
            
            gross_salary = basic_salary + HRA + other_allowances
            net_salary = gross_salary - (income_tax + employee_provident_fund)
            
            # Linear Scan Approach
            min_net_salary = net_salary[0]
            max_net_salary = net_salary[0]
            min_net_salary_employee_id = employee_id[0]
            max_net_salary_employee_id = employee_id[0]

            for i in range(1, len(net_salary)):
                if net_salary[i] < min_net_salary:
                    min_net_salary = net_salary[i]
                    min_net_salary_employee_id = employee_id[i]
                elif net_salary[i] > max_net_salary:
                    max_net_salary = net_salary[i]
                    max_net_salary_employee_id = employee_id[i]
            
            print(f"Linear Scan -> Min: ₹{min_net_salary:.2f} (ID: {min_net_salary_employee_id}), "
                  f"Max: ₹{max_net_salary:.2f} (ID: {max_net_salary_employee_id})")
            
            # Divide and conquer Approach
            def MinMaxSalary(net_salary, employee_id, left, right):
                if left == right:
                    return (net_salary[left], employee_id[left]), (net_salary[left], employee_id[left])
                if right == left + 1:
                    if net_salary[left] < net_salary[right]:
                        return (net_salary[left], employee_id[left]), (net_salary[right], employee_id[right])
                    else:
                        return (net_salary[right], employee_id[right]), (net_salary[left], employee_id[left])
                mid = left + (right - left) // 2
                (min1, min1_id), (max1, max1_id) = MinMaxSalary(net_salary, employee_id, left, mid)
                (min2, min2_id), (max2, max2_id) = MinMaxSalary(net_salary, employee_id, mid + 1, right)
                MinSalary = (min1, min1_id) if min1 < min2 else (min2, min2_id)
                MaxSalary = (max1, max1_id) if max1 > max2 else (max2, max2_id)
                return MinSalary, MaxSalary
            
            (min_net_salary, min_net_salary_employee_id), (max_net_salary, max_net_salary_employee_id) = MinMaxSalary(net_salary, employee_id, 0, len(net_salary)-1)
            
            print(f"Divide and conquer  -> Min: ₹{min_net_salary:.2f} (ID: {min_net_salary_employee_id}), "
                  f"Max: ₹{max_net_salary:.2f} (ID: {max_net_salary_employee_id})")
            print('\n')
        except Exception as e:
            print(f"  Error: {e}")

print('\nTest cases:\n')
run_test_cases()


# gross_salary = basic_salary + HRA + other_allowances
# net_salary = gross_salary - (income_tax + employee_provident_fund + professional_tax)
