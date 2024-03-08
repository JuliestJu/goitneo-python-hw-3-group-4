from field import Field


class Phone(Field):
    def __init__(self, value):
        if not self._validate_format(value):
            raise ValueError("Invalid phone number format.")
        super().__init__(value)

    @staticmethod
    def _validate_format(value):
        return len(value) == 10 and value.isdigit()
