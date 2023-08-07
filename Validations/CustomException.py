class Error(Exception):
    pass


class NullValueException(Error):
    def __init__(self, error):
        self.error = error


class FixtureException(Error):
    def __init__(self, error):
        self.error = error


class FatalException(Error):
    def __init__(self, error):
        self.error = error