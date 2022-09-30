print('='*100)
nun = list()

while True:
    nune = (int(input('Digite um valor: ')))
    if nune not in nun:
        nun.append(nune)
        print('Valor adicionado com sucesso!')
        print('='*100)
    else:
        print('Este valor já foi adicionado, tente novamente!')
    sn = str(input('Deseja adicionar outro valor? [S/N]: ')).strip().upper()
    if sn in 'Nn':
        break
print('='*100)

nun.sort()
print(f'Em ordem crescente, os números digitados por você ficam como: {nun}.')
print('='*100)
