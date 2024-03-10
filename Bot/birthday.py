from field import Field
import re


class Birthday(Field):
    def __init__(self, value):
        if not self._validate_format(value):
            raise ValueError
        else:
            super().__init__(value)

    @staticmethod
    def _validate_format(value):
        regex_pattern = r'(?:0[1-9]|[12][0-9]|3[01])[-\/.](?:0[1-9]|1[012])[-\/.](?:19\d{2}|20[01][0-9]|2020)\b'
        return bool(re.match(regex_pattern, value))
