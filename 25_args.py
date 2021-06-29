"""キーワード専用引数と位置専用引数で明確さを高める
"""

def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1.0, 10 ** 500, True, False) 
print(result) # 0

result = safe_division(1.0, 0, False, True)
print(result)  # inf

def safe_division_c(number, divisor, *,
    ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# result = safe_division_c(1.0, 10 ** 500, True, False) 
# print(result) # TypeError: safe_division() takes 2 positional arguments but 4 were given

result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float('inf')
try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    print("ZeroDivisionError")
    pass

assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) == 0.4
