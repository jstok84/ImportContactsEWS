from exchangelib import Credentials, Q, Configuration, Account, DELEGATE, Contact
from exchangelib.indexed_properties import EmailAddress, PhoneNumber, PhysicalAddress
credentials = Credentials(username='domain\\anon', password='anon')
a = Account(primary_smtp_address='anon@anon.anon', credentials=credentials, autodiscover=True, access_type=DELEGATE)
#deleteallcontacts - in mailbox under People (Not GAL!)
for item in a.contacts.all():
    item.delete()
#insertcontactinmailbox
item = Contact(account=a,
               folder=a.contacts,
               given_name='Test',
               surname='Lockt',
               display_name='Test Lockt',
               phone_numbers=[PhoneNumber(label='MobilePhone', phone_number='123456'),
                              PhoneNumber(label='BusinessPhone', phone_number='123456'),
                              PhoneNumber(label='OtherTelephone', phone_number='123456'),
                              PhoneNumber(label='Pager', phone_number='9456'),
                              PhoneNumber(label='BusinessPhone2', phone_number='123456')],
               email_addresses=[EmailAddress(label='EmailAddress1', email='test@test.si'),
                                EmailAddress(label='EmailAddress2', email='test2@test.si')],
               physical_addresses=[PhysicalAddress(label='Home',
                                                   street='Test 30',
                                                   city='TestCity',
                                                   country='TestCountry',
                                                   zipcode='8237')],
               company_name='Blue Anon Airlines',   
             )
item.save()
#printallcontacts
folder = a.root / 'AllContacts'
for p in folder.people():
    print(p)
