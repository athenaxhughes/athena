# here the variables of ENGLISH and FRENCH are defined, where the frequencies of each letter in the alphabet are stored.

ENGLISH = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357,
           0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028,
           0.0164, 0.0004)

FRENCH = (0.0840, 0.0106, 0.0303, 0.0418, 0.1726, 0.0112, 0.0127, 0.0092, 0.0734, 0.0031, 0.0005, 0.0601,
          0.0296, 0.0713, 0.0526, 0.0301, 0.0099, 0.0655, 0.0808, 0.0707, 0.0574, 0.0132, 0.0004, 0.0045,
          0.0030, 0.0012)

FREQUENCIES = (ENGLISH, FRENCH)



def cipher_message(encrypted_message, encryption_key):
    """
here the variable of cipher_message is defined, with a parameter of two arguments, encrypted_message and encryption_key
    :param encrypted_message: this parameter takes the coded message put in by the user and iterates through each character
    :param encryption_key: this parameter
    :return:
    """
    letter = ''
    ASC_A = ord('a')
    for character in encrypted_message.lower():
        if 'a' <= character <= 'z':
            letter += chr(ASC_A + (ord(character) - ASC_A + encryption_key) % 26)
        else:
            letter += character
    return letter



def delta(source, dest):
    """
    here the code produces the frequencies of delta
    :param source:
    :param dest:
    :return:
    """
    frquency_of_letter = 0.0
    for f1, f2 in zip(source, dest):
        frquency_of_letter += abs(f1 - f2)
    return frquency_of_letter



def calculate_frequency(encrypted_message):
    """
    here the variable of calculate_frequency is defined, so that the frequency of each letter is computed from a text
    :param encrypted_message: this parameter is the coded message that the user inputs at the start, which is iterated through.
    :return: the frequency of each letter in the given text is returned
    """
    dictionary = dict([(char, 0) for char in 'abcdefghijklmnopqrstuvwxyz'])
    start_frequency = 0.0
    for char in encrypted_message:
        if 'a' <= char <= 'z':
            start_frequency += 1
            dictionary[char] += 1


    length = dictionary.items()
    sorted(length)
    return [frequency / start_frequency for (length, frequency) in length]



def decipher_message(coded_message):
    """
    here the caesar cipher is deciphered by frequency analysis, as the suspected key is taken away from each letter
    :param coded_message: this parameter takes the coded message and allows the characters in it to be iterated through and the frequencies of each one to be ocunted
    :return: this returns the original coded message but with the key subtracted, creating the original message
    """
    deltamin = 1000
    bestrot = 0
    freq = calculate_frequency(coded_message)
    for encryption_key in range(26):
        dictionary = min([delta(freq[encryption_key:] + freq[:encryption_key], x) for x in FREQUENCIES])
        if dictionary < deltamin:
            deltamin = dictionary
            bestrot = encryption_key
    print("best guess key using frequency analysis is {}".format(bestrot))
    return cipher_message(coded_message, -bestrot)



import random


if __name__ == "__main__":
    user_input = input('please enter your coded message: ')
    print('the coded message is: {}'.format(user_input))
    encryption_key = random.randrange(26)
    print("encryption key used is {}".format(encryption_key))
    encrypted_text = cipher_message(user_input, encryption_key)
    print("encrypted text is '{}'".format(encrypted_text))
    print("decrypted text is '{}'".format(decipher_message(encrypted_text)))