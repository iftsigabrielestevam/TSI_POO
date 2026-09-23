'''
NIVEL 2 - APLICAÇÃO - CADASTRO COM VALIDAÇÃO
'''
# 6 ----
class SalarioInvalidoError(Exception):
    def __init__(self, salario, min):
        self.salario = salario
        self.min = min
        super().__init__(f"Salário abaixo de {self.min} não pode!")
class Funcionario:
    __minSalario = 1500

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = Funcionario.validar_salario(salario, self.__minSalario)

    @staticmethod
    def validar_salario(salario, minS):
        if salario < minS:
            raise SalarioInvalidoError(salario, minS)
        else:
            return salario

    def aumentar(self, percentual):
        if 0 < percentual <= 30:
            porcent = percentual // 100
            self._salario += self._salario * porcent
        else:
            raise ValueError("Valor Incorreto")           
try:
    f1 = Funcionario("Gabriel", 1600)
    f1.aumentar(50)
except Exception as error:
    print(f"6- {error}")
# 7 ----
import re
class EmailInvalidoError(Exception):
    def __init__(self, endereco):
        super().__init__(f"{endereco} é inválido")
class Email:
    def __init__(self, endereco):
        self.endereco = Email.validar_email(endereco)

    @staticmethod
    def validar_email(endereco):
        if re.search("@", endereco) and re.search(r"\.",endereco):
            return endereco
        else:
            raise EmailInvalidoError(endereco)
try:
    e1 = Email("gsfe1502gmail.com")
except Exception as error:
    print(f"7 - {error}")
# 9 ----














