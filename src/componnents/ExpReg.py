import re

class ExpReg:
    def __init__(self, column_name, pattern):
        self.column_name = column_name
        self.pattern = pattern
        self.regex = re.compile(pattern)

    def matches(self, text):
        return self.regex.search(text) is not None
