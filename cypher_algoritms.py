from string import ascii_lowercase
from random import choice


class LegthError(Exception):
    pass


class NotEnoughCharactersError(Exception):
    pass


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


class Morse:
    def __init__(self):
        self.codes = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                      'i': '..',
                      'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                      'r': '.-.',
                      's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
                      '0': '-----',
                      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                      '8': '---..',
                      '9': '----.'}

    def code(self, st: str) -> str:
        ans = ''
        for el in st:
            if el.lower() in self.codes.keys():
                ans += self.codes[el.lower()] + ' ' if el.lower() == el else self.codes[el.lower()].upper() + ' '
            else:
                ans += el + ' ' if el != ' ' else ''
        return ans

    def decode(self, st):
        ans = ''
        for el in st.split(' '):
            if el in self.codes.values():
                ans += get_key(self.codes, el)
            else:
                ans += el
        return ans


class Atbash:
    def __init__(self):
        self.alphabet_eng = tuple(ascii_lowercase)
        self.alphabet_rus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю",
                             "я")

    def code(self, st):
        ans = ''
        for el in st:
            if el.lower() in self.alphabet_rus:
                ans += self.alphabet_rus[(self.alphabet_rus.index(el.lower()) + 1) * -1] if el.lower() == el else \
                    self.alphabet_rus[
                        (self.alphabet_rus.index(el.lower()) + 1) * -1].upper()
            elif el.lower() in self.alphabet_eng:
                ans += self.alphabet_eng[(self.alphabet_eng.index(el.lower()) + 1) * -1] if el.lower() == el else \
                    self.alphabet_eng[
                        (self.alphabet_eng.index(el.lower()) + 1) * -1].upper()
            else:
                ans += el
        return ans

    def decode(self, st):
        return self.code(st)


def password_gen(length, contains_special_symbols, contains_numbers, contains_upper_letters, contains_lower_letters):
    alphabet = [ascii_lowercase, ascii_lowercase.upper(), '1234567890', '!@#$%^&*()—_+=;:,./?\\|`~[]{}']
    if not contains_special_symbols:
        alphabet.remove('!@#$%^&*()—_+=;:,./?\\|`~[]{}')
    if not contains_numbers:
        alphabet.remove('1234567890')
    if not contains_upper_letters:
        alphabet.remove(ascii_lowercase.upper())
    if not contains_lower_letters:
        alphabet.remove(ascii_lowercase)
    alphabet_copy, alphabet = alphabet.copy()[:], []
    for el in alphabet_copy:
        alphabet.extend(tuple(el))
    alphabet_copy = ()
    if length <= 0:
        raise LegthError('Длина пароля должна быть больше 0')
    if len(alphabet) == 0:
        raise NotEnoughCharactersError('Недостачно символов для генерации пароля')
    gen = []
    for _ in range(length):
        gen.append(choice(alphabet))
    return ''.join(gen)


codings_dict = {'Морзе': Morse(), 'Атбаш': Atbash()}
