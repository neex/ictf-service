import pwn, re, random, string

def set_flag(ip, port, flag):
    pwn.context(timeout=10)
    flag_id = "".join(random.choice(string.ascii_letters) for i in range(30))
    token = "".join(random.choice(string.ascii_letters) for i in range(30))    
    r = pwn.remote(ip, port)    
    assert r.readline() == 'Welcome to translator!\n', "Wrong banner"
    r.send("dict {}\n".format(flag_id))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in token).encode('hex') + '\n')
    assert r.readline() == "Dictionary created\n", "Can't create dictionary"
    r.send("add secretik {}\n".format(flag))
    assert r.readline() == "Word saved!\n", "Can't store word"
    r.send("quit\n")
    assert r.recvall() == "Good bye!\n", "Wrong goodbye"
    return {"FLAG_ID" : flag_id, "TOKEN" : token}
