from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def __str__(self):
        return '\n'.join(map(str, self.values()))
