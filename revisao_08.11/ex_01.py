# Nível 01 - Compressão

'''
■ 1. Classifique os relacionamentos entre:
    Pedido→Cliente, Pedido→ItemPedido, Carrinho→Produto, Pessoa→Interruptor
■ 2. O que acontece se a filha esquecer super().__init__()? Mostre/teste com código
■ 3. Sem executar: qual a saída de d.ola() no diamante D(C, B)? Como conferir?
■ 4. Por que “if isinstance(animal, Gato): ... elif ...” é um anti-padrão? Qual a alternativa?
■ 5. Qual a diferença entre um método com pass na superclasse e um @abstractmethod?
'''

# Resposta 1. Associação -> Composição -> Agregação -> Associação

# Resposta 2. -----------------------------------------------
class Pessoa():
    def __init__(self, nome):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        self.matricula = matricula # sem o super().__init__()

aluno = Aluno("João", "123")
print(aluno.nome)
# -----------------------------------------------------------

# Resposta 3. Se ele herdar este método das Super classes ascociadas, ela utilizará seguindo o MRO, portanto seria o método da classe C

# Resposta 4. Não é nada otimizado, A alternativa contra isso seria utilizar o conceito de polimofirmo quando possível

# Resposta 5. o abstractMethod obriga que a classe filha implemente o método
