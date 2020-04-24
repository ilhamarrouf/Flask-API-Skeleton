"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 17/04/20
    :time: 22.46
"""

from app import app, handler

if __name__ == "__main__":
    app.logger.addHandler(handler.log_handler())
    app.run(host="127.0.0.1", port=8000, debug=True)