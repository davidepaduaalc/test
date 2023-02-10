
class bank:
    def __init__(self,nome,code):
        self.nome= nome
        self.code = code
        self.lista_clients = []
    
    def insert(self, cliente):
        self.lista_clients.append(cliente)

    def imprime(self,cpf):
        posicao = 0
        for pessoa in self.lista_clients:
            if pessoa.cpf == cpf:
                return posicao
            posicao = posicao + 1
        print('Você não é nosso cliente ainda :s')
        return -1


class client:
    def __init__(self,nome, cpf):
            self.nome = nome
            self.cpf = cpf

    
    def consulta(self,cpf):
        print(self.nome, self.cpf)
    

def menu( banco):
    x = int(input('1-Novo Cliente\n2-Entrar conta\n3-Fechar Conta\n'))
    if x == 1:
        nome = input('Digite seu nome:')
        cpf = input('Digite seu cpf:')
        cliente = client(nome,cpf)
        banco.insert(cliente)
    elif x == 2:
        cpf = input('Digite seu cpf:')
        posicao = banco.imprime(cpf)
        if posicao > 0:
            print(banco.lista_clients[posicao].nome)
        
    else:
        print('oiii')

bancoUno = bank('banco',1377.8)
while True:
    print(bancoUno.nome, bancoUno.code)  
    menu(bancoUno)
