"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 03/05/20
    :time: 12.10
"""

def paginate(data):
    return {
        'has_next': data.has_next,
        'has_prev': data.has_prev,
        'next_num': data.next_num,
        'prev_num': data.prev_num,
        'page': data.page,
        'pages': data.pages,
        'per_page': data.per_page,
        'total': data.total,
    }