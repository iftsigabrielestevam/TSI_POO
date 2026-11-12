# Nível 02 -- Aplicação - Veículos

'''
■ 6. Veiculo(ABC): placa e diaria; calcular_aluguel(dias) abstrato; descricao() concreto
    – Carro (aluguel = diaria × dias) e Moto (20% de desconto sobre o mesmo cálculo)
    – Caminhao com taxa fixa de R$ 100 por aluguel — use super() onde couber
■ 7. Locadora que AGREGA veículos: cadastrar, faturamento_previsto(dias) polimórfico
■ 8. Prove com TypeError que Veiculo não instancia
'''

from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, placa: str, diaria: float) -> None:
        self.placa:str = placa
        self.diaria:float = diaria

    @abstractmethod
    def calcular_aluguel(self) -> None:
        pass

    def descricao(self) -> str:
        return f"| Placa: {self.placa} | Diária: {self.diaria} |"

class Carro(Veiculo):
    def calcular_aluguel(self, dias: int):
       return self.diaria * dias

class Moto(Veiculo):
    def calcular_aluguel(self, dias: int):
       return (self.diaria * dias) * 0.8

class Caminhao(Veiculo):
    def calcular_aluguel(self, dias: int):
       return (self.diaria * dias) + 100

class Locadora():
    def __init__(self) -> None:
        self.veiculos:list[Veiculo] = []

    def cadastrar(self, veiculo:Veiculo) -> None:
        self.veiculos.append(veiculo)

    def faturamento_previsto(self, dias:int) -> None:
        total:float = 0.0

        for veiculo in self.veiculos:
            total += veiculo.calcular_aluguel(dias)

        return total
