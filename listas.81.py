nune = []

while True:
    nun = (int(input('Digite um valor: ')))
    nune.append(nun)
    sn = str(input('Deseja adicionar outro valor? [S/N]: ')).strip().upper()
    if sn in 'Nn':
        break
print('='*100)

#a)
print(f'Essa lista tem {len(nune)} números')
print('='*100)

#b)
nune.sort(reverse=True)
print(f'Os números digitados por você ficam como {nune} em ordem decrescente.')
print('='*100)

#c)
if 5 in nune:
    print('O valor 5 foi digitado por você!')
else:
    print('O valor 5 não foi digitado por você na lista!')
print('='*100)