from assistant_bot import AssistantBot


def main():
    print("Welcome to the assistant bot!")
    bot = AssistantBot()

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
        elif command == "add-birthday":
            print(bot.add_birthday(args))
        elif command == "show-birthday":
            print(bot.show_birthday(args))
        elif command == "birthdays":
            print(bot.birthdays())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

