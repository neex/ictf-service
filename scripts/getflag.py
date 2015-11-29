import pwn, re, random, string

def get_flag(ip, port, flag_id, token):
    pwn.context(timeout=10)
    r = pwn.remote(ip, port)
    if not r.readline() == 'Welcome to translator!\n':
        raise RuntimeError("Wrong banner")
    r.send("dict {}\n".format(flag_id))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    if not m:
        raise RuntimeError("Wrong password request")
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in token).encode('hex') + '\n')
    if not r.readline() == 'Password ok!\n':
        raise RuntimeError("Can't load dictionary")
    if not r.readline() == 'Dictionary loaded\n':
        raise RuntimeError("Can't load dictionary")
    r.send("translate secretik\n")
    flag = r.readline().strip()
    if not flag != "secretik":
        raise RuntimeError("Flag not present or deleted")
    r.send("quit\n")
    if not r.recvall() == "Good bye!\n":
        raise RuntimeError("Wrong goodbye")
    return {"FLAG" : flag}
