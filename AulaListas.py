nome = ['Goku','Vegeta', 'Trunks', 'Gohan'] #Lista

#INSERT
nome.append('Bulma') # insere no final
nome.insert(2, 'Piccolo') #insere em posição desejada
print(nome)

#UPDATE
nome[0] =  'Gohan' #coloca onde queremos

#DELETE
del nome[1] #excluindo pelo indice / nome.pop(1)
nome.remove('Trunks') #excluindo pela string
print(nome)

if 'Piccolo' in nome:
    print('Piccolo está aqui')