"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 22/04/20
    :time: 09.49
"""

import string
import random


def _random(size=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(size))
