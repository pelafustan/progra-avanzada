class Encryptor:
    def __init__(self):
        self.encoded = ''

    def set_encrypt(self, number):
        number = str(number)
        enc = ''
        for i in range(len(number)):
            f = 7
            for j in range(i+1):
                f += int(number[j])
            if f >= 10:
                f %= 10
            enc += str(f)
        self.encoded = enc[2] + enc[3] + enc[0] + enc[1]

    def get_encrypt(self):
        return self.encoded


if __name__ == "__main__":
    encryptor = Encryptor()
    number = 1234
    print("El número que se encriptará es {}".format(number))
    encryptor.set_encrypt(number)
    print("El número ya encriptado es {}".format(encryptor.get_encrypt()))
