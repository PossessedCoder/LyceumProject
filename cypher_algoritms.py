from string import ascii_lowercase
from random import choice


class LegthError(Exception):
    pass


class NotEnoughCharactersError(Exception):
    pass


def morse(st: str) -> str:
    codes = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
             'r': '.-.',
             's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
             '0': '-----',
             '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..',
             '9': '----.'}
    ans = ''
    for el in st:
        if el in codes:
            ans += codes[el] if el.lower() == el else codes[el].upper()
        else:
            ans += el
    return ans


def atbash(st: str) -> str:
    alphabet_eng = tuple(ascii_lowercase)
    alphabet_rus = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю",
                    "я")
    ans = ''
    for el in st:
        if el.lower() in alphabet_rus:
            ans += alphabet_rus[(alphabet_rus.index(el.lower()) + 1) * -1] if el.lower() == el else alphabet_rus[
                (alphabet_rus.index(el.lower()) + 1) * -1].upper()
        elif el.lower() in alphabet_eng:
            ans += alphabet_eng[(alphabet_eng.index(el.lower()) + 1) * -1] if el.lower() == el else alphabet_rus[
                (alphabet_rus.index(el.lower()) + 1) * -1].upper()
        else:
            ans += el
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
    alphabet_copy = ()
    if length <= 0:
        raise LegthError('Длина пароля должна быть больше 0')
    if len(alphabet) == 0:
        raise NotEnoughCharactersError('Недостачно символов для генерации пароля')
    gen = []
    for _ in range(length):
        gen.append(choice(alphabet))
    return ''.join(gen)


codings_dict = {'Морзе': morse, 'Атбаш': atbash}
