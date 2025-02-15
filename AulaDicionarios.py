#A diferença é o oindice ser personalizado
#Chave:Valor


pessoa = {'nome': 'Goku', 'idade': 42}
print(pessoa)  # Acessa o elemento
print(pessoa['nome'])  # Insere uma chave e atribui o valor nome

pessoa['sexo'] = 'M'
pessoa['nome'] = 'Vegeta'
del pessoa['sexo']
print(pessoa)