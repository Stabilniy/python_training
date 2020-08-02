from modules.contact import Contact
import random
import string
import getopt
import sys
import os.path
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of group", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + '_'.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Contact(firstname= random_string("firstname", 15 ), middlename = random_string("middlename", 10), lastname = random_string("lastname", 20) , nickname = random_string("nickname", 13) , title = random_string("title", 12) , company = random_string("company", 11) , address = random_string("address", 14) , home = random_string("home", 21), mobile = random_string("mobile", 10),
                                              work = random_string("work", 11), fax = random_string("fax", 10), email = random_string("email", 18) , email1 = random_string("email1", 12), email2 = random_string("email2", 21) , email3 = random_string("email3", 10), address2 = random_string("address2", 17) , homepage = random_string("homepage", 14), phone2 = random_string("phone2", 10), notes = random_string("notes", 14)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
