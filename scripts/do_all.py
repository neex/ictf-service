from setflag import set_flag
from getflag import get_flag
from benign import benign
from exploit import exploit
import random, string

flag = "FLG" + "".join(random.choice(string.ascii_letters + string.digits) for i in xrange(20))
print flag
x = set_flag('162.243.124.166', 12343, flag)
print x
y = get_flag('162.243.124.166', 12343, x['FLAG_ID'], x['TOKEN'])
assert flag == y["FLAG"]
print y
benign('162.243.124.166', 12343)
z = exploit('162.243.124.166', 12343, x['FLAG_ID'])
assert flag == z["FLAG"]
print z

