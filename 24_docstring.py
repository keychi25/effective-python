"""動的なデフォルト引数を指定する時にはNoneとdocstringを使う
- デフォルト引数は一度しか評価されない．
    {}，[]，datetime.now()などを使用する時は注意が必要
"""



from time import sleep
from datetime import datetime

def log(message, when=None):
    """Log a message with a timestamp．

    Args:
        message：Message to print
        when：datetime of when the message occured．
            Defailts to the present time．
    """
    if when is None:
        when = datetime.now()
    print(f'{when}：{message}')

log('Hi there!')
sleep(0.1)
log('Hi again!')