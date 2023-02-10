#sorteador amigo oculto 
import random

class Pessoa:
    def __init__(self,nome,number):
            self.nome = nome
            self.number = number
            self.situation = False
            self.ident = int(number)
            self.check = False
    
    def display_name(self):
        print(self.nome, '\n')
   
def sorteio(participantes, i, lista_part):
    while lista_part[i].check == False:   
        if i == (participantes - 2):
            if lista_part[(participantes - 1)].situation == False:
                lista_part[i].ident = participantes - 1
                lista_part[i].check = True
                return 

        lista_part[i].ident = random.randint(0,(participantes - 1))
        if lista_part[lista_part[i].ident].situation == False and lista_part[i].ident != i : 
            lista_part[lista_part[i].ident].situation = True
            lista_part[i].check == True 
            return

participantes = int(input('Quantas pessoas irão participar?'))
lista_part = []
for i in range(participantes):
    nome = input('Digite o nome:') 
    lista_part.append(Pessoa(nome,i))

for j in range(participantes):
    sorteio((participantes),j,lista_part)

for k in range(participantes):
    print(lista_part[k].nome, '->', lista_part[lista_part[k].ident].nome)
    #lista_part[lista_part[k].ident].display_name()




    


