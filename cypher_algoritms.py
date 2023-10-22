from string import ascii_lowercase


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


codings_dict = {'Морзе': morse, 'Атбаш': atbash}
