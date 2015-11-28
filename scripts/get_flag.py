import pwn, re, random, string

def get_flag(ip, port, flag_id, token):
    pwn.context(timeout=10)
    r = pwn.remote(ip, port)    
    assert r.readline() == 'Welcome to translator!\n', "Wrong banner"
    r.send("dict {}\n".format(flag_id))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in token).encode('hex') + '\n')
    assert r.readline() == 'Password ok!\n', "Can't load dictionary"
    assert r.readline() == 'Dictionary loaded\n', "Can't load dictionary"    
    r.send("translate secretik\n")
    flag = r.readline().strip()
    assert flag != "secretik", "Flag not present or deleted"
    r.send("quit\n")
    assert r.recvall() == "Good bye!\n", "Wrong goodbye"
    return {"FLAG" : flag}

