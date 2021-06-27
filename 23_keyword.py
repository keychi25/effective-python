"""キーワード引数にオプションの振る舞いを与える
"""
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

remainder(20, 7) # OK
remainder(20, divisor=7) # OK
remainder(number=20, divisor=7) # OK
remainder(divisor=7, number=20) # OK
# remainder(number=20, 7) # SyntaxError: positional argument follows keyword argument
# remainder(20, number=7) # TypeError: remainder() got multiple values for argument 'number'

my_kwargs = {
    'number': 20,
    'divisor': 7,
}
assert remainder(**my_kwargs) == 6 # 辞書の内容を使って引数に渡す時は，**演算子を使用する．

my_only_divisor_kwargs = {
    'divisor': 7,
}
assert remainder(number=20, **my_only_divisor_kwargs) == 6 # 朝服が無ければ，**演算子と位置引数または木ワード引数と混在可能

def print_paramrters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}={value}')
print_paramrters(alpha=1.5, beta=9, gamma=4)