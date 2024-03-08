from assistant_bot import AssistantBot

# Task2


def main():
    bot = AssistantBot()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = bot.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(bot.add_contact(args))
        elif command == "change":
            print(bot.change_contact_phone(args))
        elif command == "phone":
            print(bot.display_contact_phone(args))
        elif command == "all":
            print(bot.display_all_contacts())
        else:
            print("Invalid command.")

