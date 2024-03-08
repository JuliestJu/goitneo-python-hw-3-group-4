# goitneo-python-hw-3-group-4

Task #1

It's time to combine our previous homework into one.

You have to add extra functionality to your classes:

Add a field for birthday - the Birthday class. This field is optional, but there can be only one.
Let's add the functionality of working with Birthday to the Record class, particularly the add_birthday function, which adds a birthday to a contact.
Let's add the checking functionality to correct the entered values for the Phone and Birthday fields.
Let's add our function to the AddressBook class from the first homework assignment. This function is the get_birthdays_per_week, which returns a list of users who must be congratulated for the contacts in the address book the following week.
Now, your bot should operate with the functionality of the AddressBook class. This means that instead of the contacts dictionary, we use a book = AddressBook()

To implement the new functionality, also add handlers with the following commands:

add-birthday — add a birthday to the contact in the format DD.MM.YYYY.
show-birthday — show the contact's birthday.
birthdays — returns a list of users who need to be congratulated on days in the next week
So, our bot should support the following list of commands:

add [name] [phone]: Add a new contact with a name and phone number.
change [name] [new phone]: Change the phone number for the specified contact.
phone [name]: Show the phone number for the specified contact.
all: Show all contacts in the address book.
add-birthday [name] [birth date]: Add a date of birth for the specified contact.
show-birthday [name]: Show the date of birth for the specified contact.
birthdays: Show birthdays that will take place within the next week.
hello: Receive a greeting from a bot.
close or exit: Close the app.
Evaluation criteria:

Implement all the specified commands to the bot.
All data should be output in a clear and user-friendly format.
All errors, such as incorrect input or missing contact, should be adequately handled with an appropriate message to the user.
Data validation:
The date of birth should be in the format DD.MM.YYYY.
The phone number must consist of 10 digits.
The program should be closed correctly after executing the close or exit commands.
