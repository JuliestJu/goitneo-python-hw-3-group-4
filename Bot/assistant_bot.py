from decorators import InputErrorDecorator


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @InputErrorDecorator.input_error
    def add_contact(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    @InputErrorDecorator.input_error
    def change_contact_phone(self, args):
        name, phone = args
        if name in self.contacts:
            self.contacts[name] = phone
            return "Phone number updated."
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def display_contact_phone(self, args):
        name = args[0]
        if name in self.contacts:
            return f"{name}'s phone number: {self.contacts[name]}"
        else:
            return "Contact not found."

    @InputErrorDecorator.input_error
    def display_all_contacts(self):
        if self.contacts:
            result = "All contacts:\n"
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result.strip()
        else:
            return "No contacts available."
