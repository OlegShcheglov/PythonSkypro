from address import Address
from Mailing import Mailing

from_address = Address("624130", "Novouralsk", "Frunze", 2, 25)
to_address = Address("672027", "Chita", "Nechaeva", 68, 39)

mail_to = Mailing(to_address, from_address, 550, str(10002569871110))

print(mail_to)
