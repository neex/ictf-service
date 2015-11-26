/^ *$/ b;

/^help$/ {
  s/.*/ Commands allowed:\n  translate <text>\n    translate line of text\n\n  dict <dictionary name>\n    load or create private dictionary\n\n  add <word> <translation>\n    add word to loaded private dictionary\n\n  help\n     print this help\n\n  quit\n     quit/p;
  b;
};

/^quit$/ {
  s/.*/Good bye!/p;
  q 0;
};

/^translate / {
  s/^translate //;
  s/[^[:print:]]//g;
  s/'/'"'"'/g;
  s#^.*$#echo '&' | sed -r -f ../ro/common.sed#;
  G;
  /\n$/ {
    s/\n//;
  }
  s/\n/ -f /;
  s/.*/&/ep;
  b;
};


/^add / {
  x;
  /^$/ {
     s/.*/You need to load or create dictionary first/p;
     s/.*//;
     h;
     b;
  };
  x;
  s/add //;
  /^[A-Za-z0-9]+ +[A-Za-z0-9]+$/! {
      s/.*/Can't parse word or replacement! Only a-zA-Z0-9 are allowed/p;
      b;
  }
  s#^([A-Za-z0-9]+) +([A-Za-z0-9]+)$#s/\1/\2/gi;#;
  G;
  s#(.*)\n(.*)#echo '\1' >> \2#e;
  s#.*#Word saved!#p;
  b;
};

/^dict / {
  s/^dict //;
  /[^A-Za-z0-9_]/ {
    s/.*/Invalid dictionary name! Only A-Z, a-z, 0-9 and _ are allowed./p;
    b;
  }
  h;
  s#.*#dd if=/dev/urandom count=1 bs=1000 status=none | base64#e;
  s/^.*([A-F0-9]).*([A-F0-9]).*$/\1\2/;
  s/.*/Please enter your alphanumeric password xored with byte 0x& and hex encoded:/p;
  s/^.*0x(..).*/\1/;
  H;
  n;
  /[^0-9A-Fa-f]/ {
    s/.*/Please input only hexadecimal characters/p;
    b bad;
  }
  /^$/ {
    s/.*/Password cannot be blank!/p;
    b bad;
  }
  s/../&-/g;
  /-.$/ {
    s/.*/Odd number of characters/p;
    b bad;
  }
  H;
  g;
  s/^[^\n]*\n//;
:addxorbyte
  s/(..)\n(.*)-/\1\n\2\1=/;
  t addxorbyte;
  s/.*\n//;
  s/([A-F0-9])([A-F0-9])([A-F0-9])([A-F0-9])=/\1\3-\2\4-=/gi;
  s/00-/0/gi;s/01-/1/gi;s/02-/2/gi;s/03-/3/gi;s/04-/4/gi;s/05-/5/gi;s/06-/6/gi;s/07-/7/gi;s/08-/8/gi;s/09-/9/gi;s/0a-/a/gi;s/0b-/b/gi;s/0c-/c/gi;s/0d-/d/gi;s/0e-/e/gi;s/0f-/f/gi;s/10-/1/gi;s/11-/0/gi;s/12-/3/gi;s/13-/2/gi;s/14-/5/gi;s/15-/4/gi;s/16-/7/gi;s/17-/6/gi;s/18-/9/gi;s/19-/8/gi;s/1a-/b/gi;s/1b-/a/gi;s/1c-/d/gi;s/1d-/c/gi;s/1e-/f/gi;s/1f-/e/gi;s/20-/2/gi;s/21-/3/gi;s/22-/0/gi;s/23-/1/gi;s/24-/6/gi;s/25-/7/gi;s/26-/4/gi;s/27-/5/gi;s/28-/a/gi;s/29-/b/gi;s/2a-/8/gi;s/2b-/9/gi;s/2c-/e/gi;s/2d-/f/gi;s/2e-/c/gi;s/2f-/d/gi;s/30-/3/gi;s/31-/2/gi;s/32-/1/gi;s/33-/0/gi;s/34-/7/gi;s/35-/6/gi;s/36-/5/gi;s/37-/4/gi;s/38-/b/gi;s/39-/a/gi;s/3a-/9/gi;s/3b-/8/gi;s/3c-/f/gi;s/3d-/e/gi;s/3e-/d/gi;s/3f-/c/gi;s/40-/4/gi;s/41-/5/gi;s/42-/6/gi;s/43-/7/gi;s/44-/0/gi;s/45-/1/gi;s/46-/2/gi;s/47-/3/gi;s/48-/c/gi;s/49-/d/gi;s/4a-/e/gi;s/4b-/f/gi;s/4c-/8/gi;s/4d-/9/gi;s/4e-/a/gi;s/4f-/b/gi;s/50-/5/gi;s/51-/4/gi;s/52-/7/gi;s/53-/6/gi;s/54-/1/gi;s/55-/0/gi;s/56-/3/gi;s/57-/2/gi;s/58-/d/gi;s/59-/c/gi;s/5a-/f/gi;s/5b-/e/gi;s/5c-/9/gi;s/5d-/8/gi;s/5e-/b/gi;s/5f-/a/gi;s/60-/6/gi;s/61-/7/gi;s/62-/4/gi;s/63-/5/gi;s/64-/2/gi;s/65-/3/gi;s/66-/0/gi;s/67-/1/gi;s/68-/e/gi;s/69-/f/gi;s/6a-/c/gi;s/6b-/d/gi;s/6c-/a/gi;s/6d-/b/gi;s/6e-/8/gi;s/6f-/9/gi;s/70-/7/gi;s/71-/6/gi;s/72-/5/gi;s/73-/4/gi;s/74-/3/gi;s/75-/2/gi;s/76-/1/gi;s/77-/0/gi;s/78-/f/gi;s/79-/e/gi;s/7a-/d/gi;s/7b-/c/gi;s/7c-/b/gi;s/7d-/a/gi;s/7e-/9/gi;s/7f-/8/gi;s/80-/8/gi;s/81-/9/gi;s/82-/a/gi;s/83-/b/gi;s/84-/c/gi;s/85-/d/gi;s/86-/e/gi;s/87-/f/gi;s/88-/0/gi;s/89-/1/gi;s/8a-/2/gi;s/8b-/3/gi;s/8c-/4/gi;s/8d-/5/gi;s/8e-/6/gi;s/8f-/7/gi;s/90-/9/gi;s/91-/8/gi;s/92-/b/gi;s/93-/a/gi;s/94-/d/gi;s/95-/c/gi;s/96-/f/gi;s/97-/e/gi;s/98-/1/gi;s/99-/0/gi;s/9a-/3/gi;s/9b-/2/gi;s/9c-/5/gi;s/9d-/4/gi;s/9e-/7/gi;s/9f-/6/gi;s/a0-/a/gi;s/a1-/b/gi;s/a2-/8/gi;s/a3-/9/gi;s/a4-/e/gi;s/a5-/f/gi;s/a6-/c/gi;s/a7-/d/gi;s/a8-/2/gi;s/a9-/3/gi;s/aa-/0/gi;s/ab-/1/gi;s/ac-/6/gi;s/ad-/7/gi;s/ae-/4/gi;s/af-/5/gi;s/b0-/b/gi;s/b1-/a/gi;s/b2-/9/gi;s/b3-/8/gi;s/b4-/f/gi;s/b5-/e/gi;s/b6-/d/gi;s/b7-/c/gi;s/b8-/3/gi;s/b9-/2/gi;s/ba-/1/gi;s/bb-/0/gi;s/bc-/7/gi;s/bd-/6/gi;s/be-/5/gi;s/bf-/4/gi;s/c0-/c/gi;s/c1-/d/gi;s/c2-/e/gi;s/c3-/f/gi;s/c4-/8/gi;s/c5-/9/gi;s/c6-/a/gi;s/c7-/b/gi;s/c8-/4/gi;s/c9-/5/gi;s/ca-/6/gi;s/cb-/7/gi;s/cc-/0/gi;s/cd-/1/gi;s/ce-/2/gi;s/cf-/3/gi;s/d0-/d/gi;s/d1-/c/gi;s/d2-/f/gi;s/d3-/e/gi;s/d4-/9/gi;s/d5-/8/gi;s/d6-/b/gi;s/d7-/a/gi;s/d8-/5/gi;s/d9-/4/gi;s/da-/7/gi;s/db-/6/gi;s/dc-/1/gi;s/dd-/0/gi;s/de-/3/gi;s/df-/2/gi;s/e0-/e/gi;s/e1-/f/gi;s/e2-/c/gi;s/e3-/d/gi;s/e4-/a/gi;s/e5-/b/gi;s/e6-/8/gi;s/e7-/9/gi;s/e8-/6/gi;s/e9-/7/gi;s/ea-/4/gi;s/eb-/5/gi;s/ec-/2/gi;s/ed-/3/gi;s/ee-/0/gi;s/ef-/1/gi;s/f0-/f/gi;s/f1-/e/gi;s/f2-/d/gi;s/f3-/c/gi;s/f4-/b/gi;s/f5-/a/gi;s/f6-/9/gi;s/f7-/8/gi;s/f8-/7/gi;s/f9-/6/gi;s/fa-/5/gi;s/fb-/4/gi;s/fc-/3/gi;s/fd-/2/gi;s/fe-/1/gi;s/ff-/0/gi;
  /00=/ {
     s/.*/Zero byte in password! You think that's cool?/p;
     b bad;
  }
  s/0A=//;
  s/(..)=/\\x\1/gi;
  x;
  s/([^\n]*)\n.*$/\1/;
  H;
  s#.*#head -n 1 '&' 2>/dev/null#e;
  /^$/ {
    g;
    s|(.*)\n(.*)|/bin/echo -e '#\1' > \2|e;
    g;
    s/^.*\n([^\n]*)$/\1/;
    h;
    s/.*/Dictionary created/p;
    b;
  }
  H;
  g;
  s|^([^\n]*)\n.*|/bin/echo -e '\1'|e;
  H;
  g;
  s/^[^\n]*\n([^\n]*)\n.*/\1/;
  x;
  s/^[^\n]*\n[^\n]*\n//;
  /^#(.*)\n\1/ {
      s/.*/Password ok!\nDictionary loaded/p;
      b;
  }
  s/.*/Dictionary exists and password doesn't match/p;
:bad
  s/.//g;
  h;
  s/.*/Dictionary not loaded/p;
  b;
};

s/^([^ ]*)/Unknown command or invalid argument number: \1/p;
