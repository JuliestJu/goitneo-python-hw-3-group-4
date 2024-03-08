from decorators import InputErrorDecorator
from AddressBook.address_book import AddressBook


class AssistantBot:
    def __init__(self):
        self.addressBook = AddressBook()

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @staticmethod
    def display_response(response):
        print(response)

    @InputErrorDecorator.input_error
    def add_contact(self, args):
        name, phone, birthday = args
        record = Record(name, phone, birthday)
        self.addressBook.add_record(record)
        return "Contact added."

    @InputErrorDecorator.input_error
    def change_contact_phone(self, args):
        name, phone = args
        record = self.addressBook.find(name)
        if record:
            record.phones = [phone]
            return "Phone number updated."
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def display_contact_phone(self, args):
        name = args[0]
        record = self.addressBook.find(name)
        if record:
            return f"{name}'s phone number: {', '.join(map(str, record.phones))}"
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def display_all_contacts(self):
        return str(self.addressBook)

    @InputErrorDecorator.input_error
    def add_birthday(self, args):
        name, date = args
        record = self.addressBook.find(name)
        if record:
            record.add_birthday(date)
            return "Birthday added."
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def show_birthday(self, args):
        name = args[0]
        record = self.addressBook.find(name)
        if record and record.name.birthday:
            return f"{name}'s birthday: {record.name.birthday}"
        else:
            return "Birthday not found."

    @InputErrorDecorator.input_error
    def birthdays(self):
        birthdays_next_week = self.addressBook.get_birthdays_per_week()
        if birthdays_next_week:
            return f"Birthdays to congratulate next week: {', '.join(birthdays_next_week)}"
        else:
            return "No birthdays next week."
