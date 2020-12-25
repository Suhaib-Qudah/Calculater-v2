from contact_book import ContactBook
from contact import Contact

def generate_contacts():
    #create a contact book
    my_contacts = ContactBook ()

    contact = Contact("abdallah","mestarihi","abbd","abd@gmail.com")
    contact1 = Contact("laith","zagal","lol2", "laith@gmail.com")
    contact2 = Contact("shadi","melhem","sh213", "shadi@gmail.com")
    
    #add contacts to contacts book
    my_contacts.add_contact(contact)
    my_contacts.add_contact(contact1)
    my_contacts.add_contact(contact2)

    return my_contacts