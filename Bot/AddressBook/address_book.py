from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.now()
        next_week = today + timedelta(days=7)

        birthdays_next_week = []
        for record in self.values():
            if record.birthday:
                contact_birthday = datetime.strptime(str(record.birthday), "%d.%m.%Y")
                if today <= contact_birthday < next_week:
                    birthdays_next_week.append(str(record.name))

        return birthdays_next_week

    def __str__(self):
        return '\n'.join(map(str, self.values()))
