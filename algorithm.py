class TextCaesar:
    def __init__(self, text):
        self.text = text

    def encrypt(self):
        # Equation enc : (plain - key) % 256
        key = int(input('Enter a key: '))
        enc_list = []

        # Text to ASCII and change value with caesar cipher
        for values in self.text:
            ASCII = int(ord(values))
            enc_list.append((ASCII + key) % 256)
        # print(enc_list)

        # After converted, ASCII value transformized to text again
        cipherized = ''.join(chr(i) for i in enc_list)
        print('The cipher from message is: "' + cipherized + '"')

    def decrypt(self):
        # Equation dec : (plain + key) % 256
        key = int(input('Enter a key: '))
        dec_list = []

        for values in self.text:
            ASCII = int(ord(values))
            dec_list.append((ASCII - key) % 256)
        # print(dec_list)

        decipherized = ''.join(chr(i) for i in dec_list)
        print('The message from cipher is: "' + decipherized + '"')