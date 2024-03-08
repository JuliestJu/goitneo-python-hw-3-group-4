from name import Name
from phone import Phone
from birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if str(phone) != phone_number]

    def edit_phone(self, old_phone, new_phone):
        if old_phone in [str(phone) for phone in self.phones]:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)

    def find_phone(self, phone_number):
        return [phone for phone in self.phones if str(phone) == phone_number]

    def add_birthday(self, date):
        if not self.birthday:
            self.birthday = Birthday(date)
        else:
            print("A birthday already exists for this contact.")

    def __str__(self):
        birthday_info = f", Birthday: {self.birthday}" if self.birthday else ""
        return f"Name: {self.name}{birthday_info}, Phones: {', '.join(map(str, self.phones))}"
