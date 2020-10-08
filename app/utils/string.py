"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 22/04/20
    :time: 09.49
"""

import string
import random


def _random(size=8, punctuation=False):
    letters = string.ascii_letters + string.digits

    if punctuation:
        letters += string.punctuation

    return ''.join(random.choice(letters) for i in range(size))
