from sys import maxsize

class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None , nickname = None, title = None, company = None, address = None, home = None, mobile = None, work = None, fax = None, email = None, email1 = None, email2 = None, email3 = None,
                 address2 = None, homepage = None, bday = None, bmounth = None, byear = None, aday = None, amonth = None, ayear = None, phone2 = None, notes = None, id = None, all_phones = None, all_emails = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.homepage = homepage
        self.bday = bday
        self.bmounth = bmounth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.all_emails, self.all_phones, self.address)

    def __eq__(self, other):
        return self.address == other.address and self.all_phones == other.all_phones and self.all_emails == other.all_emails and self.firstname == other.firstname and self.lastname == other.lastname and self.company == other.company and (self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


