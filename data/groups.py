from modules.group import Group
import random
import string


testdata = [Group(name="testname1569", header="testheader15478", footer="testfooter101478")]

'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + '_'.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(name="testname", header="testheader", footer="testfooter")] + [
             Group(name = random_string("name", 10), header= random_string("header", 20), footer = random_string("footer", 15)) for i in range(2)]

'''