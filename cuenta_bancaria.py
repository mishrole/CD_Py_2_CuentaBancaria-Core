class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance = 0):
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        self.tasa_interés = tasa_interés
        self.balance = balance
        self.tarifa = 5
    # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def depósito(self, amount):
        # tu código aquí
        self.balance += amount
        print(f'Haciendo un depósito de {amount:.2f}')
        return self
    def retiro(self, amount):
        # tu código aquí
        if(self.balance - amount < 0):
            print("Fondos insuficientes")
        else:
            print(f'Realizando un retiro de {amount:.2f}')
            print(f'Cobrando una tarifa de {self.tarifa:.2f}')
            self.balance -= amount + self.tarifa
        return self
    def mostrar_info_cuenta(self):
        # tu código aquí
        print(f'Balance: {self.balance:.2f}')
        return self
    def generar_interés(self):
        # tu código aquí
        if(self.balance > 0):
            interes = self.balance * self.tasa_interés
            self.balance += interes
            print(f'Generando un interés de {interes:.2f}')
        else:
            print('Balance negativo, no genera interés')
        return self

cuenta1 = CuentaBancaria(tasa_interés = 0.01)
cuenta1.depósito(500).depósito(500).depósito(1000).retiro(500).generar_interés().mostrar_info_cuenta()
cuenta2 = CuentaBancaria(tasa_interés = 0.01)
cuenta2.depósito(1000).depósito(3000).retiro(200).retiro(400).retiro(600).retiro(800).generar_interés().mostrar_info_cuenta()