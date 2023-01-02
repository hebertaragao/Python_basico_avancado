
from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return[tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return[Tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao] [0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes())'



class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes())'


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passsar roupa')
    casa.add('Lavar prato')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add("Carne")
    mercado.add("Toamte")
    print(mercado)

    for tarefa in  mercado.tarefas:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()
