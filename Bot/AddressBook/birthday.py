import re
from field import Field


class Birthday(Field):
    def __init__(self, date):
        super().__init__(date)
        self.validate_date_format()

    def validate_date_format(self):

        pattern = re.compile(r'(^0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(\d{4}$)')

        if not pattern.match(str(self.value)):
            print("Invalid date format for Birthday. Please use DD.MM.YYYY.")
            self.value = None
