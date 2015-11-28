import pwn, re, random, string

def benign(ip, port):
    def rand_str():
        return ''.join(random.choice(string.ascii_letters) for i in range(30))
    pwn.context(timeout=10)
    word_cnt = random.randrange(3, 10)
    words = []
    for i in range(word_cnt):
        words.append([rand_str(), rand_str(), rand_str()])
    dict_id1 = rand_str()
    pwd1 = rand_str()
    dict_id2 = rand_str()
    pwd2 = rand_str()
    str_to_translate = " ".join([x[0] for x in words])
    str_after_translate_1 = " ".join([x[1] for x in words])
    str_after_translate_2 = " ".join([x[2] for x in words])
    str_without_translate = str_to_translate

    r = pwn.remote(ip, port)
    assert r.readline() == 'Welcome to translator!\n', "Wrong banner"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_without_translate, "Wrong default translation"
    r.send("dict {}\n".format(dict_id1))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in pwd1).encode('hex') + '\n')
    assert r.readline() == "Dictionary created\n", "Can't create dictionary 1"
    for (word_from, word_to1, word_to2) in words:
        r.send("add {} {}\n".format(word_from, word_to1))
        assert r.readline() == "Word saved!\n", "Can't store word"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_after_translate_1, "Wrong translation after adding words"

    r.send("dict {}\n".format(dict_id2))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in pwd2).encode('hex') + '\n')
    assert r.readline() == "Dictionary created\n", "Can't create dictionary 2"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_without_translate, "Wrong translation after switching dictionaries"
    for (word_from, word_to1, word_to2) in words:
        r.send("add {} {}\n".format(word_from, word_to2))
        assert r.readline() == "Word saved!\n", "Can't store word"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_after_translate_2, "Wrong translation after adding words to another dictionary"

    r.send("quit\n")
    assert r.recvall() == "Good bye!\n", "Wrong goodbye"


    r = pwn.remote(ip, port)
    assert r.readline() == 'Welcome to translator!\n', "Wrong banner"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_without_translate, "Wrong default translation after words added to another dictionary"
    r.send("dict {}\n".format(dict_id1))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in pwd2).encode('hex') + '\n')
    assert r.readline() == "Dictionary exists and password doesn't match\n", "Wrong message after wrong password"
    assert r.readline() == "Dictionary not loaded\n", "Wrong message after wrong password"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_without_translate, "Wrong translation after wrong password attempt"

    r.send("dict {}\n".format(dict_id1))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(pwd1 + 'XXX\n')
    assert r.readline() == 'Please input only hexadecimal characters\n', "Wrong message after invalid password"
    assert r.readline() == "Dictionary not loaded\n", "Wrong message after invalid password"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_without_translate, "Wrong translation after invalid password attempt"

    r.send("dict {}\n".format(dict_id1))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in pwd1).encode('hex') + '\n')
    assert r.readline() == 'Password ok!\n', "Can't load dictionary"
    assert r.readline() == 'Dictionary loaded\n', "Can't load dictionary"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_after_translate_1, "Wrong translation after loading stored dictionary"

    r.send("dict {}\n".format(dict_id2))
    info = r.readline()
    m = re.match("Please enter your alphanumeric password xored with byte 0x([0-9A-F]{2}) and hex encoded:\n", info)
    assert m, "Wrong password request"
    byte = int(m.group(1), 16)
    r.send(''.join(chr(ord(c) ^ byte) for c in pwd2).encode('hex') + '\n')
    assert r.readline() == 'Password ok!\n', "Can't load dictionary"
    assert r.readline() == 'Dictionary loaded\n', "Can't load dictionary"
    r.send("translate {}\n".format(str_to_translate))
    assert r.readline().strip() == str_after_translate_2, "Wrong translation after loading stored dictionary"

    r.send("quit\n")
    assert r.recvall() == "Good bye!\n", "Wrong goodbye"
