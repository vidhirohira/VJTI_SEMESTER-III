def partial_product(x, y):
    x_str, y_str = str(x), str(y)
    products = []
    for i, digit_y in enumerate(reversed(y_str)):
        row = int(digit_y) * x * (10 ** i)
        products.append(row)
    return sum(products)

x = 9619184233
y = 9820174446
result = partial_product(x, y)
print(result)


