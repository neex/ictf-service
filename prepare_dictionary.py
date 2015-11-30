#!/usr/bin/env python3

import re

import requests
import transliterate

GSL = "http://jbauman.com/gsl.html"

YANDEX_API_KEY = "trnsl.1.1.20151129T233700Z.c2adc604d41dada6.16363497b0b202eccceee672885b10d5e4a61825"

def get_words():
    res = requests.get(GSL)
    for line in res.iter_lines():
        m = re.match(r'^(?P<rank>\d+) (?P<freq>\d+) (?P<word>.*)<BR>$', line.strip().decode('ascii'))
        if m:
            yield m.group('word')

def translate_word(word):
    params = {
        'key': YANDEX_API_KEY,
        'lang': 'en-ru',
        'text': word,
    }
    res = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=params)

    return transliterate.translit(res.json()['text'][0], 'ru', reversed=True)

def main():
    words = list(get_words())
    for word in words:
        print(r"s|\b{}\b|{}|g".format(word.lower(), translate_word(word).lower()))


if __name__ == '__main__':
    main()
