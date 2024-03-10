from datetime import datetime, timedelta
from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, name, phone):
        print(name, phone)
        record = Record(name)
        record.add_phone(phone)
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.now()
        next_week_start = today + timedelta(days=(7 - today.weekday()))
        next_week_end = next_week_start + timedelta(days=7)

        birthdays_next_week = []

        for record in self.values():
            if record.birthday:
                birthday_date = datetime.strptime(str(record.birthday), '%d.%m.%Y')
                if next_week_start <= birthday_date < next_week_end:
                    birthdays_next_week.append(record)

        return birthdays_next_week

    def __str__(self):
        return '\n'.join(map(str, self.values()))
