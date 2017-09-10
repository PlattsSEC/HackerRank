#!/usr/bin/python3.5
from collections import OrderedDict


class KeyWordTranspositionCipher(object):
    def __init__(self, key, word):
        self.alphabet = ''.join(list(map(chr, range(65, 91))))
        self.key = key.upper()
        self.word = word.upper()

    def _remove_duplicates(self) -> str:
        return ''.join(OrderedDict.fromkeys(self.key))

    def _remove_chars_from_alphabet(self) -> str:
        letters = self._remove_duplicates()
        return ''.join(
            [letter for letter in self.alphabet if letter not in letters])

    def _encrypt(self, word: str, key: str) -> str:
        return_text = []
        for char in word:
            if char == ' ':
                return_text.append(char)
                continue
            position = key.index(char)
            return_text.append(self.alphabet[position])
        return ''.join(return_text)

    def encrypt(self) -> str:

        self.key = self._remove_duplicates()
        new_alphabet = self._remove_chars_from_alphabet()
        new_key = ''
        for i in range(len(self.key)):
            new_key += self.key[i]
            for j in range(i, len(new_alphabet), len(self.key)):
                new_key += new_alphabet[j]
            new_key += " "
        new_key = new_key.split(" ")
        new_key.sort()
        new_key = ''.join([x for x in new_key[1:]])
        self.key = ''.join(sorted(self.key))
        print(self.key)

        return self._encrypt(self.word, new_key)


if __name__ == '__main__':

    word = 'jhqsu xfxbq'  # input('Enter a word: ')
    key = 'secret'  # input('Enter a key: ')

    ktc = KeyWordTranspositionCipher(key, word)
    secret = ktc.encrypt()
    print(secret)

    word = 'LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK'  # input('Enter a word: ')
    key = 'SPORT'  # input('Enter a key: ')

    ktc = KeyWordTranspositionCipher(key, word)
    secret = ktc.encrypt()
    print(secret)
