"""
    __mising__でキー依存デフォルト値を作成する方法を把握しておく
"""
def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Faild to open path {profile_path}')
        raise
path = 'proile_1234.png'

class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        print(value)
        return value


from collections import defaultdict
pictures = defaultdict(open_picture)
handle = pictures[path] # TypeError: open_picture() missing 1 required positional argument: 'profile_path'
handle.seek(0)
image_data = handle.read()

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
