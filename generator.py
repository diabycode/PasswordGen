import string
from random import randint
import random

class PasswordGenerator:

    def generate(self, alpha_len, digit_len, special_len):
        p = self.get_alpha(alpha_len) + self.get_digit(digit_len) + self.get_special(special_len)
        random.shuffle(p)
        passwd = "".join(p)
        return passwd

    def get_alpha(self, length):
        list_alpha = [l for l in string.ascii_lowercase+string.ascii_uppercase]
        l = []
        for i in range(length):
            alea_n = randint(0, len(list_alpha)-1)
            l.append(list_alpha[alea_n])
        return l

    def get_digit(self, length):
        digit = [str(n) for n in range(10)]
        l = []
        for i in range(length):
            alea_n = randint(0, len(digit)-1)
            l.append(digit[alea_n])
        return l

    def get_special(self, length):
        special_carac = "@ ! # $ % ^ & * ? ~ :".split(" ")
        l = []
        for i in range(length):
            alea_n = randint(0, len(special_carac)-1)
            l.append(special_carac[alea_n])
        return l


# def main():
#     alpha_len = input("Nombre de caractere alphabetique: ")
#     digit_len = input("Nombre de caractere numerique: ")
#     special_len = input("Nombre de caractere special: ")

#     c = Caracter()
#     passwd = c.get_alpha(int(alpha_len)) + c.get_digit(int(digit_len)) + c.get_special(int(special_len))
#     random.shuffle(passwd)
#     passwd = "".join(passwd)

#     print(passwd)


    





if __name__ == "__main__":
    # typer.run(main)
    pg = PasswordGenerator()
    pass_ = pg.generate(alpha_len=5, digit_len=9, special_len=1)
    print(pass_)