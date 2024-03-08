from address_book import AddressBook
from record import Record

book = AddressBook()

# Creation of entry for John
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")

# Add a John entry to the address book
book.add_record(john)

# Creating and adding a new entry for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Adding a birthday for John
john.add_birthday("12.03.1990")

# Displaying all entries in the contact list
for name, record in book.data.items():
    print(record)

    # Find and edit a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555, Birthday: 15.03.1990

# Searching for a specific phone number in John's entry
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Showing John's birthday
print(f"{john.name}'s birthday: {john.birthday}")

# Displaying birthdays for the next week
print(f"Birthdays next week: {book.get_birthdays_per_week()}")

# Deletion Jane's entry
book.delete("Jane")
