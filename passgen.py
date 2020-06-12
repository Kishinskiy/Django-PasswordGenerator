import string
import random





if __name__ == '__main__':
    chars = string.ascii_lowercase

    chars = chars + string.ascii_uppercase

    chars.__add__(string.digits)

    chars.__add__(string.punctuation)

    print(chars)