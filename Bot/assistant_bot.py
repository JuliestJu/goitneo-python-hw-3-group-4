from decorators import InputErrorDecorator
from Bot.address_book import AddressBook


class AssistantBot:
    def __init__(self):
        self.address_book = AddressBook()

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @InputErrorDecorator.input_error
    def add_contact(self, args):
        name, phone = args
        self.address_book.add_record(name, phone)
        return "Contact added."

    @InputErrorDecorator.input_error
    def add_birthday(self, args):
        name, birthday_date = args
        print(name)
        print(birthday_date)
        record = self.address_book.find(name)
        if record:
            record.add_birthday(birthday_date)
            return "Birthday added."
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def show_birthday(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if record and record.birthday:
            return f"{name}'s birthday: {record.birthday}"
        else:
            return "Contact not found or no birthday available."

    @InputErrorDecorator.input_error
    def birthdays(self):
        birthdays_next_week = self.address_book.get_birthdays_per_week()
        if birthdays_next_week:
            result = "Birthdays in the next week:\n"
            for record in birthdays_next_week:
                result += f"{record.name}: {record.birthday}\n"
            return result.strip()
        else:
            return "No birthdays in the next week."

    @InputErrorDecorator.input_error
    def change_contact_phone(self, args):
        name, old_phone, new_phone = args
        record = self.address_book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            return "Phone number updated."
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def display_contact_phone(self, args):
        name = args[0]
        record = self.address_book.find(name)

        if record and record.phones:
            phones_str = ', '.join(map(str, record.phones))
            return f"{name}'s phones numbers: {phones_str}"
        else:
            return "Contact not found"

    @InputErrorDecorator.input_error
    def display_all_contacts(self):
        return str(self.address_book)

