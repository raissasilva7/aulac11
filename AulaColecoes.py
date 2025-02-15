#Tupla é imutavel, não pode alterar ou excluir elementos
nome = ('Goku','Vegeta', 'Trunks', 'Gohan') #Tupla
print(nome)

#SLICING DE DADOS (recorte de dados)
print(nome[0]) #Goku
print(nome[:2]) #Goku e Vegeta
#No Python, o 1° indice de uma coleção é INCLUSIVE
#No Python, o 2° indice de uma coleção é ENCLUSIVE

print(nome[2:]) #Trunks e Gohan
print(nome[1:3]) #Vegeta e Trunks

print(nome[-1]) #Gohan
#No Python, se colocar indice - ele le de tras para frente

print(len(nome)) # quantia de nomes