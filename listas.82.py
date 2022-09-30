nune = list()
par = list()
impar = list()

while True:
    nun = (int(input('Digite um valor: ')))
    nune.append(nun)
    sn = str(input('Deseja adicionar outro valor? [S/N]: ')).strip().upper()
    if sn in 'Nn':
        break
print('='*100)

#impar par
for ind, val in enumerate(nune):
    if val % 2 == 0:
        par.append(val)
    elif val % 2 == 1:
        impar.append(val)
print('='*100)

#resultado
print(f'A lista completa é: {nune}.')
print(f'Todos os números pares desta lista são {par}')
print(f'Todos os números ímpares desta lista são {impar}')