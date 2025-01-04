def NormalMultiplication(x, y):
    """Perform normal multiplication of two large integers represented as strings."""
    n1 = len(x)
    n2 = len(y)
    
    # Check for zero inputs
    if x == "0" or y == "0":
        return "0"
    
    # Initialize result list
    prod = ['0'] * (n1 + n2)
    
    # Multiply each digit
    for i in range(n1 - 1, -1, -1):
        carry = 0
        for j in range(n2 - 1, -1, -1):
            product = int(x[i]) * int(y[j])
            total = product + carry + int(prod[i + j + 1])
            prod[i + j + 1] = str(total % 10)
            carry = total // 10
        prod[i + j] = str(int(prod[i + j]) + carry)
    
    # Join and remove leading zeros
    final = ''.join(prod).lstrip('0')
    return final if final else "0"


def Karatsuba(x: str, y: str) -> int:
    """Perform Karatsuba multiplication of two large integers represented as strings."""
    sign1 = -1 if x[0] == '-' else 1
    sign2 = -1 if y[0] == '-' else 1
    x = x.lstrip('-')
    y = y.lstrip('-')
    final_sign = sign1 * sign2
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    
    if n == 1:
        return final_sign * (int(x) * int(y))
    
    mid = n // 2
    x1, x0 = x[:mid], x[mid:]
    y1, y0 = y[:mid], y[mid:]
    
    p1 = Karatsuba(x1, y1)
    p2 = Karatsuba(x0, y0)
    
    a = str(int(x1) + int(x0))
    b = str(int(y1) + int(y0))
    ab = Karatsuba(a, b)
    
    p3 = ab - p1 - p2
    return final_sign * (10 ** (2 * (n - mid)) * p1 + 10 ** (n - mid) * p3 + p2)

def is_integer(string: str) -> bool:
    """Check if the input string represents a valid integer."""
    if string.startswith('-'):
        return string[1:].isdigit()  # Check if it's a negative integer
    return string.isdigit()  # Check if it's a positive integer


# Input and output
x = input("Enter First Number: ")
y = input("Enter the Second Number: ")
if not is_integer(x) or not is_integer(y):
    print("INVALID INPUT")
else:
    print(f"Product by Normal Multiplication is {NormalMultiplication(x, y)}")
    print(f"Product by Karatsuba Multiplication is {Karatsuba(x, y)}")
