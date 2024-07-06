# Arithmetic Operators
a = 10
b = 5

print("Arithmetic Operators:")
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation
print(f"{a} // {b} = {a // b}")  # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print(f"{a} == {b} -> {a == b}")  # Equal to
print(f"{a} != {b} -> {a != b}")  # Not equal to
print(f"{a} > {b} -> {a > b}")  # Greater than
print(f"{a} < {b} -> {a < b}")  # Less than
print(f"{a} >= {b} -> {a >= b}")  # Greater than or equal to
print(f"{a} <= {b} -> {a <= b}")  # Less than or equal to

# Logical Operators
x = True
y = False

print("\nLogical Operators:")
print(f"{x} and {y} -> {x and y}")  # Logical AND
print(f"{x} or {y} -> {x or y}")  # Logical OR
print(f"not {x} -> {not x}")  # Logical NOT

# Assignment Operators
c = 10
print("\nAssignment Operators:")
print(f"c = {c}")  # Assignment
c += 5
print(f"c += 5 -> {c}")  # Add and assign
c -= 3
print(f"c -= 3 -> {c}")  # Subtract and assign
c *= 2
print(f"c *= 2 -> {c}")  # Multiply and assign
c /= 4
print(f"c /= 4 -> {c}")  # Divide and assign
c %= 3
print(f"c %= 3 -> {c}")  # Modulus and assign
c **= 2
print(f"c **= 2 -> {c}")  # Exponent and assign
c //= 2
print(f"c //= 2 -> {c}")  # Floor division and assign

# Bitwise Operators
d = 6  # binary: 110
e = 2  # binary: 010

print("\nBitwise Operators:")
print(f"{d} & {e} -> {d & e}")  # Bitwise AND
print(f"{d} | {e} -> {d | e}")  # Bitwise OR
print(f"{d} ^ {e} -> {d ^ e}")  # Bitwise XOR
print(f"~{d} -> {~d}")  # Bitwise NOT
print(f"{d} << 1 -> {d << 1}")  # Bitwise left shift
print(f"{d} >> 1 -> {d >> 1}")  # Bitwise right shift
