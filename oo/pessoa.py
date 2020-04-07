class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':

    luiz = Pessoa(nome='Luiz')
    spurio = Pessoa(luiz, nome='Spurio')
    print(Pessoa.cumprimentar(spurio))
    print(id(spurio))
    print(spurio.cumprimentar())
    print(spurio.nome)
    for filho in spurio.filhos:
        print(filho.nome)
    spurio.sobrenome = "Antonio"
    del spurio.filhos
    luiz.olhos = 1
    del luiz.olhos
    print(spurio.__dict__)
    print(luiz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(spurio.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(luiz.olhos), id(spurio.olhos))