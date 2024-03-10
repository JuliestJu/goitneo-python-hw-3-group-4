from datetime import datetime, timedelta
from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, name, phone):
        str_name = str(name)

        if str_name in self.data:
            existing_record = self.data[str_name]
            existing_record.add_phone(phone)
        else:
            record = Record(name)
            record.add_phone(phone)
            self.data[str_name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        birthdays_per_week = []

        for record in self.data.values():
            if self.is_within_next_week(record.birthday.value):
                birthdays_per_week.append(record)

        return birthdays_per_week

    def is_within_next_week(self, date_string):
        input_date = datetime.strptime(date_string, '%d.%m.%Y')
        today = datetime.now()

        days_difference = (input_date.replace(year=today.year) - today).days
        return 0 <= days_difference <= 7

    def __str__(self):
        return '\n'.join(map(str, self.values()))
