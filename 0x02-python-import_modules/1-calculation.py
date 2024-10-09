#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

sum_result = add(a, b)
difference_result = sub(a, b)
product_result = mul(a, b)
quotient_result = div(a, b)

print("Sum: {}".format(sum_result))
print("Difference: {}".format(difference_result))
print("Product: {}".format(product_result))
print("Quotient: {}".format(quotient_result))
