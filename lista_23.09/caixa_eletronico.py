import os
class ErroDeConta(Exception):
    def __init__(self, text):
            super().__init__(text)
class ValorInvalidoError(ErroDeConta):
    def __init__(self):
        super().__init__(f"Valor inválido")
class SaldoInsuficienteError(ErroDeConta):
    def __init__(self):
        super().__init__(f"Saldo é insuficiente")
class LimiteExcedidoError(ErroDeConta):
    def __init__(self):
        super().__init__(f"Limite de Saque Excedido")
class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor < 1:
            raise ValorInvalidoError
        else:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 1000 or valor < 0:
            raise LimiteExcedidoError
        elif valor > self._saldo:
            raise SaldoInsuficienteError
        else:
            self._saldo -= valor
os.system('cls')
conta = None
while True:
    try:
        print("1 - Criar Conta \n" \
            "2 - Depositar \n" \
            "3 - Sacar \n" \
            "4 - Saldo \n" \
            "5 - Sair" )
        opc = int(input(": "))
        match opc:
            case(1):
                conta = ContaBancaria()
                os.system('cls')
                print("Conta criada\n")
                continue
                
            case(2):
                if not isinstance(conta, ContaBancaria):
                    os.system('cls')
                    print("Conta não foi criada\n")
                    continue    
                else:
                    os.system('cls')
                    conta.depositar(int(input("Quanto deseja depositar: ")))
                    print("")
            case(3):
                if not isinstance(conta, ContaBancaria):
                    os.system('cls')
                    print("Conta não foi criada\n")
                    continue
                else:
                    os.system('cls')
                    conta.sacar(int(input("Quanto deseja sacar: ")))
            case(4):
                if not isinstance(conta, ContaBancaria):
                    os.system('cls')
                    print("Conta não foi criada\n")
                    continue
                else:
                    os.system('cls')
                    print(f"Saldo na conta: {conta.saldo} \n")
            case(5):
                os.system('cls')
                print("Saindo...\n")
                break
    except Exception as error:
        os.system('cls')
        print(f"Error: [{error}] Sistema Reiniciado!\n")


