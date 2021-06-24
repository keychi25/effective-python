"""
    辞書の欠損キーの処理にはinやKeyErrorではなくgetを使う
"""

counters = {
    'pumpernickel': 2,
    'sourdough': 1
}

print('------------------------')
print(f"Base Dict ：{counters}")
print('------------------------')

# inでの実装
key_of_in = 'croissant' # countersのkeyにないもの
if key_of_in in counters:
    count = counters[key_of_in]
else:
    count = 0
counters[key_of_in] = count + 1

print('------------------------')
print(f"Added Dict of in：{counters}")
print('------------------------')

# Keyerrorでの実装
key_of_key_error = 'wheat' # countersのkeyにないもの
try:
    count = counters[key_of_key_error]
except KeyError:
    count = 0
counters[key_of_key_error] = count + 1

print('------------------------')
print(f"Added Dict of KeyError：{counters}")
print('------------------------')

# getでの実装
key_of_get = 'financier' # countersのkeyにないもの
count = counters.get(key_of_get, 0)
counters[key_of_get] = count + 1

print('------------------------')
print(f"Added Dict of get：{counters}")
print('------------------------')

print('値が配列の時')
# valueが配列の場合
votes = {
    'pumpernickel': ['Bob', 'Alice'],
    'sourdough': ['Coco', 'Deb' ]
}

# inでの実装
key_of_in_array = 'brioche' # votesのkeyにないもの
who_of_in = 'Elmer'
if key_of_in_array in votes:
    names = votes[key_of_in_array]
else:
    votes[key_of_in_array] = names = []
names.append(who_of_in)

print('------------------------')
print(f"Added Dict in Array of in：{votes}")
print('------------------------')

# KeyErrorでの実装
key_of_key_error_array = 'kanure' # votesのkeyにないもの
who_of_key_error = 'francis'
try:
    names = votes[key_of_key_error_array]
except KeyError:
    votes[key_of_key_error_array] = names = []
names.append(who_of_key_error)

print('------------------------')
print(f"Added Dict in Array of KeyError：{votes}")
print('------------------------')

# getでの実装
key_of_get_array = 'kouign-amann' # votesのkeyにないもの
who_of_get = 'george'


if (names := votes.get(key_of_get_array) ) is None: # 代入式で繰り返しを防ぐ（項目10）
    votes[key_of_get_array] = names = []
names.append(who_of_get)

print('------------------------')
print(f"Added Dict in Array of get：{votes}")
print('------------------------')

print('setdefaultを使用した場合')
print('------------------------')
key_of_setdefault = 'setdefault'
who_of_setdefault = 'setdefault'

names = votes.setdefault(key_of_setdefault, [])
names.append(who_of_setdefault)

print('------------------------')
print(f"Added Dict in Array of setdefault：{votes}")
print('------------------------')