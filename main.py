import pickle

# Define a Contact class to represent individual contacts
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
            return contacts
    except FileNotFoundError:
        return []

# Function to search for contacts by name or phone number
def search_contacts(contacts, query):
    results = []
    for contact in contacts:
        if query in contact.name or query in contact.phone:
            results.append(contact)
    return results

def main():
    # Load contacts from a file
    contacts = load_contacts('contacts.pkl')

    while True:
        print("Options:")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contacts.append(new_contact)
            print("Contact added successfully!")

        elif choice == '2':
            query = input("Enter search query: ")
            search_results = search_contacts(contacts, query)

            if search_results:
                print("Search results:")
                for result in search_results:
                    print(result)
            else:
                print("No matching contacts found.")

        elif choice == '3':
            # Save contacts and exit
            save_contacts('contacts.pkl', contacts)
            print("Contacts saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
