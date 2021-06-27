"""可変長位置変数を使って，見た目をスッキリさせる
"""
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}:{values_str}')
    
log('My numbers are', 1, 2)
log('Hi there')

favorites = [7, 33, 9]
log('Favorite colors', *favorites) # 可変個引数関数を呼びだす[タプルに変換される]
log('Favorite colors', favorites)  # 配列自体を引数にする

def my_generator():
    for i in range(10):
        yield i
def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)