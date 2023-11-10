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
                ans += el + ' ' if el != ' ' else ' '
        return ans.rstrip()

    def decode(self, st):
        ans = ''
        for el in st.split(' '):
            if el in self.codes.values():
                ans += get_key(self.codes, el)
            else:
                ans += el if el != '' else ' '
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


class Ceaser:
    def __init__(self):
        self.alphabet_eng = tuple(ascii_lowercase)
        self.alphabet_rus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю",
                             "я")

    def code(self, st, key):
        ans = ''
        for el in st:
            if el.lower() in self.alphabet_rus:
                ans += self.alphabet_rus[
                    (self.alphabet_rus.index(el.lower()) + key) % len(self.alphabet_rus)] if el == el.lower() else \
                    self.alphabet_rus[(self.alphabet_rus.index(el.lower()) + key) % len(self.alphabet_rus)].upper()
            elif el.lower() in self.alphabet_eng:
                ans += self.alphabet_eng[
                    (self.alphabet_eng.index(el.lower()) + key) % len(self.alphabet_eng)] if el == el.lower() else \
                    self.alphabet_eng[(self.alphabet_eng.index(el.lower()) + key) % len(self.alphabet_eng)].upper()
            else:
                ans += el
        return ans

    def decode(self, st, key):
        ans = ''
        for el in st:
            if el.lower() in self.alphabet_rus:
                ans += self.alphabet_rus[
                    (self.alphabet_rus.index(el.lower()) - key) % len(self.alphabet_rus)] if el == el.lower() else \
                    self.alphabet_rus[(self.alphabet_rus.index(el.lower()) - key) % len(self.alphabet_rus)].upper()
            elif el.lower() in self.alphabet_eng:
                ans += self.alphabet_eng[
                    (self.alphabet_eng.index(el.lower()) - key) % len(self.alphabet_eng)] if el == el.lower() else \
                    self.alphabet_eng[(self.alphabet_eng.index(el.lower()) - key) % len(self.alphabet_eng)].upper()
            else:
                ans += el
        return ans


class Vigener:
    def __init__(self):
        self.alphabet_eng = tuple(ascii_lowercase)
        self.alphabet_rus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю",
                             "я")

    def code(self, st, key):
        ans = ''
        key = [self.alphabet_eng.index(el) if el in self.alphabet_eng else self.alphabet_rus.index(el) for el in
               key.lower() if el in self.alphabet_eng or el in self.alphabet_rus]
        for i, el in enumerate(st):
            if el.lower() in self.alphabet_rus:
                ans += self.alphabet_rus[
                    (self.alphabet_rus.index(el.lower()) + key[i % len(key)]) % len(
                        self.alphabet_rus)] if el == el.lower() else \
                    self.alphabet_rus[
                        (self.alphabet_rus.index(el.lower()) + key[i % len(key)]) % len(self.alphabet_rus)].upper()
            elif el.lower() in self.alphabet_eng:
                ans += self.alphabet_eng[
                    (self.alphabet_eng.index(el.lower()) + key[i % len(key)]) % len(
                        self.alphabet_eng)] if el == el.lower() else \
                    self.alphabet_eng[
                        (self.alphabet_eng.index(el.lower()) + key[i % len(key)]) % len(self.alphabet_eng)].upper()
            else:
                ans += el
        return ans

    def decode(self, st, key):
        ans = ''
        key = [self.alphabet_eng.index(el) if el in self.alphabet_eng else self.alphabet_rus.index(el) for el in
               key.lower() if el in self.alphabet_eng or el in self.alphabet_rus]
        for i, el in enumerate(st):
            if el.lower() in self.alphabet_rus:
                ans += self.alphabet_rus[
                    (self.alphabet_rus.index(el.lower()) - key[i % len(key)]) % len(
                        self.alphabet_rus)] if el == el.lower() else \
                    self.alphabet_rus[
                        (self.alphabet_rus.index(el.lower()) - key[i % len(key)]) % len(self.alphabet_rus)].upper()
            elif el.lower() in self.alphabet_eng:
                ans += self.alphabet_eng[
                    (self.alphabet_eng.index(el.lower()) - key[i % len(key)]) % len(
                        self.alphabet_eng)] if el == el.lower() else \
                    self.alphabet_eng[
                        (self.alphabet_eng.index(el.lower()) - key[i % len(key)]) % len(self.alphabet_eng)].upper()
            else:
                ans += el
        return ans


class Vernam:
    def __init__(self):
        pass

    def code(self, st, key):
        ans = []
        st = [bin(ord(el)) for el in st]
        key = [bin(ord(el)) for el in key]
        for i, el in enumerate(st):
            ans.append(int(el, 2) ^ int(key[i], 2))
        ans = ' '.join([chr(el) for el in ans])
        return ans


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
    alphabet_copy = None
    if length <= 0:
        raise LegthError('Длина пароля должна быть больше 0')
    if len(alphabet) == 0:
        raise NotEnoughCharactersError('Недостачно символов для генерации пароля')
    gen = []
    for _ in range(length):
        gen.append(choice(alphabet))
    return ''.join(gen)


# print(Vernam().code('LONDON', 'SYSTEM'))
codings_dict = {'Морзе': (Morse(), []), 'Атбаш': (Atbash(), []), 'Шифр Цезаря': (Ceaser(), ['keyn']),
                'Шифр Виженера': (Vigener(), ['keyw'])}
codings_info = {
    'Морзе': 'Способ знакового кодирования, в котором буквы алфавита, цифры, знаки препинания и другие символы представляются в виде последовательностей коротких и длинных сигналов, называемых точками и тире.',
    'Атбаш': 'Простой шифр подстановки для алфавитного письма. Правило шифрования состоит в замене i -й буквы алфавита буквой с номером n − i + 1 , где n — число букв в алфавите.',
    'Шифр Цезаря': 'Разновидность шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите.',
    'Шифр Виженера': 'Метод является усовершенствованным шифром Цезаря, где буквы смещались на определенную позицию. Шифр Виженера состоит из последовательности нескольких шифров Цезаря с различными значениями сдвига.'}
