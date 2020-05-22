class Card:
    def __init__(self, balance=0):
        self.saldo = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def discount(self, debt):
        self.set_balance(self.get_balance() - debt)
        if self.get_saldo() < 0:
            print("Saldo insuficiente para realizar la transacción.")


if __name__ == "__main__":
    tarjeta = Card(9001)
    print("El saldo de la tarjeta es ${}.".format(tarjeta.get_balance))
    tarjeta.discount(100)
    print("Se debitaron $100 de su cuenta. El nuevo saldo es ${}."
          .format(tarjeta.get_balance()))
