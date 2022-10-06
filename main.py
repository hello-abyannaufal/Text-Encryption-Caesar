from algorithm import TextCaesar

print('===========================[WELCOME TO CAESAR ENCRYPTION]==========================='
      '\n1. Encryption Text'
      '\n2. Decryption text')
method = int(input('Input method: '))

if method == 1:
    plain = input('Input your message here: ')
    caesar = TextCaesar(plain)
    caesar.encrypt()

elif method == 2:
    cipher = input('Enter the cipher: ')
    caesar = TextCaesar(cipher)
    caesar.decrypt()