"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 06/05/20
    :time: 05.33
"""

from app import rq, app

if __name__ == '__main__':
    rq.get_scheduler(interval=app.config['RQ_SCHEDULER_INTERVAL']).run()