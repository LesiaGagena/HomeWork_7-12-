import json

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, filename):
        data = {
            'contacts': [
                {'name': contact.name, 'phone_number': contact.phone_number}
                for contact in self.contacts
            ]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.contacts = [
                Contact(contact['name'], contact['phone_number'])
                for contact in data['contacts']
            ]

    def search_contacts(self, search_string):
        matching_contacts = []
        for contact in self.contacts:
            if search_string.lower() in contact.name.lower() or search_string in contact.phone_number:
                matching_contacts.append(contact)
        return matching_contacts
      
      
