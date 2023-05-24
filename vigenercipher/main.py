class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def __get_key(self,text):
        return self.key*(len(text)//len(self.key)) + self.key[:len(text)%len(self.key)]

    def encode(self, text):
        key = self.__get_key(text)
        encoded_word = ''
        for letter,key_letter in zip(text,key):
            if not letter in self.alphabet:
                encoded_word = encoded_word + letter
                continue
            encrypt_letter = self.alphabet[self.alphabet.index(key_letter):] + \
                             self.alphabet[:self.alphabet.index(key_letter)]
            encoded_word = encoded_word + encrypt_letter[self.alphabet.index(letter)]

        return encoded_word
    def decode(self, text):
        key = self.__get_key(text)
        decoded_word = ''
        for letter, key_letter in zip(text, key):
            if not letter in self.alphabet:
                decoded_word = decoded_word + letter
                continue
            decrypt_letter = self.alphabet[self.alphabet.index(key_letter):] + \
                             self.alphabet[:self.alphabet.index(key_letter)]
            decoded_word = decoded_word + self.alphabet[decrypt_letter.index(letter)]
        return decoded_word
