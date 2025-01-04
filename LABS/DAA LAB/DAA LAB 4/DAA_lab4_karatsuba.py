def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    max_len = max(len(str(x)), len(str(y)))
    half_len = max_len // 2

    x_high = x // 10**half_len
    x_low = x % 10**half_len
    y_high = y // 10**half_len
    y_low = y % 10**half_len

    z0 = karatsuba(x_low, y_low)       
    z1 = karatsuba(x_high, y_high)      
    z2 = karatsuba(x_low + x_high, y_low + y_high)  

    
    return (z1 * 10**(2 * half_len)) + ((z2 - z1 - z0) * 10**half_len) + z0


if __name__ == "__main__":
    x = int("10" * 500)  
    y = 0
    result = karatsuba(x, y)
    print(f"The product of \n{x}\n and \n{y}\n is \n{result}.")

