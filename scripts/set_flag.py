import pwn, re, random, string

def set_flag(ip, port, flag):
    pwn.context(timeout=10)
    flag_id = "".join(random.choice(string.ascii_letters) for i in range(30))
    token = "".join(random.choice(string.ascii_letters) for i in range(30))    
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
    if not r.readline() == "Dictionary created\n":
        raise RuntimeError("Can't create dictionary")
    r.send("add secretik {}\n".format(flag))
    if not r.readline() == "Word saved!\n":
        raise RuntimeError("Can't store word")
    r.send("quit\n")
    if not r.recvall() == "Good bye!\n":
        raise RuntimeError("Wrong goodbye")
    return {"FLAG_ID" : flag_id, "TOKEN" : token}
