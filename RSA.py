import math


def encr(func):
    def inner(self, x, y):
        if y == 1:
            print("The encrypted ", end="")
        func(self, x, y)
    return inner


def decr(func):
    def inner(self, x, y):
        if y == 2:
            print("The decrypted ", end="")
        func(self, x, y)
    return inner


class RSA:

    def __init__(self):
        self.e = 0
        self.d = 0
        self.List = []

    def messages(self):
        N = self.keyGen(self.inputFunc())
        e_list = []
        for i in self.List:
            x = self.encrypt(i, N)
            e_list.append(x)
            self.printFunc(x, 1)

        for i in e_list:
            x = self.decrypt(i, N)
            self.printFunc(x, 2)

    @decr
    @encr
    def printFunc(self, number, y):
        print("message is " + str(number))

    def inputFunc(self):
        x = int(input("Enter the number of messages: "))
        print("Enter the messages:")
        for i in range(x):
            self.List.insert(i, int(input()))
        return int(input("Enter the minimum value for the prime numbers: "))

    def primeGen(self, number):
        nnumber = number
        prime = False
        while prime is False:
            prime = True
            nnumber = nnumber + 1
            for i in range(2, int(math.sqrt(nnumber) + 1)):
                if nnumber % i == 0:
                    prime = False
                    break
        return nnumber

    def keyGen(self, number):
        q = self.primeGen(number)
        p = self.primeGen(q)
        N = p * q
        TN = (p - 1) * (q - 1)
        for i in range(2, TN):
            if math.gcd(i, TN) == 1:
                self.e = i
                break
        lt = TN
        rt = TN
        lb = self.e
        rb = 1
        while lb != 1:
            nlb = lt - math.floor(lt / lb) * lb
            nrb = rt - math.floor(lt / lb) * rb
            lt = lb
            lb = nlb
            rt = rb
            rb = nrb
            if lb < 0:
                lb = lb % TN
            if rb < 0:
                rb = rb % TN
        self.d = rb
        print("N is " + str(N))
        print("e is " + str(self.e))

        return N

    def encrypt(self, number, N):
        return pow(number, self.e, N)

    def decrypt(self, number, N):
        return pow(number, self.d, N)


if __name__ == '__main__':
    rsa = RSA()
    rsa.messages()
