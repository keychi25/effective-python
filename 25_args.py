"""専用引数と位置専用引数で明確さを高める
- キーワード専用引数，引用リストの１つの*の後として定義される．
- 引数リストの起動 / と *の間にある引数は，位置でもキーワードでも渡せる．

[それぞれの利点]
- キーワード専用引数：複数の論理型フラグを使う場合など，紛らわしい関数呼び出しの際に，
    呼び出し元に強制的にキーワード引数を与えることで意図が明確になる．
- 位置専用引数：引数名への依存性を減らすことができる．
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


def safe_division_d(numerator, denominator, /, *,
    ignore_overflow=False, ignore_zero_division=False):
    """位置専用引数として設定
    """
    try:
        return numerator / denominator
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

assert safe_division_d(2, 5) == 0.4
# safe_division_d(numerator=2, denominator=5) # TypeError: safe_division_d() got some positional-only arguments passed as keyword arguments: 'numerator, denominator'


def safe_division_e(numerator, denominator, /,
    ndigits=10, *,
    ignore_overflow=False, ignore_zero_division=False):
    """位置専用引数として設定
    """
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
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

result = safe_division_e(22, 7)
print(result)

result = safe_division_e(22, 7, 5)
print(result)


result = safe_division_e(22, 7, ndigits=2)
print(result)