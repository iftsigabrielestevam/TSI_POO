import random

print("")
print("QUESTÃO 01 ===================")
print("")

class Aluno:
    def __init__(self, nome:str, matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def __str__(self):
        return (f"{self.nome}({self.matricula})")

    def lancar_nota(self, valor:float):
        self.notas.append(valor)

    @staticmethod
    def media(notas) -> float:
        return sum(notas) / len(notas)

    def aprovado(self) -> bool:
        if Aluno.media(self.notas) >= 6:
            return True
        else:
            return False

alunos = [
    Aluno("Jamile","1285483"),
    Aluno("Gabriel","42142421"),
    Aluno("Ana","4215161")
]

for i in alunos:
    i.lancar_nota(random.randint(0,10))
    i.lancar_nota(random.randint(0,10))
    if i.aprovado():
        print(i)

print("")
print("QUESTÃO 02 ===================")
print("")

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.base + 2 * self.altura
    
    def __eq__(self, outro):
        if( outro.area() + outro.perimetro() == self.area() + self.perimetro() ):
            return True
        else:
            return False

ret1 = Retangulo(4, 5)
ret2 = Retangulo(4, 5)    
print(ret1 == ret2)

print("")
print("QUESTÃO 03 ===================")
print("")

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, data):
        [dia, mes, ano] = data.split("/")
        return cls(dia, mes, ano)

data = Data.de_texto("01/20/2007")
print(data.dia)
print(data.mes)
print(data.ano)