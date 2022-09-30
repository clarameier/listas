print('='*100)
nomind = []
real = []
maior = menor = 0
while True:
    nomind.append(str(input('Digite um nome: ')))
    nomind.append(float(input('Digite o peso desta pessoa: ')))
   
    if len(real) == 0:
        maior = menor = nomind[1]
    else:
        if nomind[1] > maior:
            maior = nomind[1]
        if nomind[1] < menor:
            menor = nomind[1]

    print('-'*100)
    real.append(nomind[:])
    nomind.clear()
    sn = str(input('Deseja adicionar outro valor? [S/N]: ')).strip().upper()
    if sn in 'Nn':
        break
print('='*100)

#listagem
print(f'Os dados finais foram {real}.')
print('='*100)

#a)
print(f'Foram cadastradas {len(real)} pessoas.')
print('='*100)

#b)
print(f'Os maiores pesos cadastrados foram respectivamente: {maior}kg. ')
for p in real:
    if p[1] == maior:
        print(f'Peso este da(o): {p[0]}')
print('='*100)

#c)
print(f'Os menores pesos cadastrados foram respectivamente: {menor}kg.')
for p in real:
    if p[1] == menor:
        print(f'Peso este da(o): {p[0]}')
print('='*100)