from werkzeug.exceptions import Unauthorized


class AuthenticationHttpException(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.status_code = Unauthorized.code
        self.message = 'These credentials do not match our records.'
        self.errors = {'username': ['These credentials do not match our records.']}