print('='*100)
nuns = []
nuns.append(5)
nuns.append(9)
nuns.append(4)

for n in nuns:
    print(f'{n} -> ', end='')
print('fim')
print('='*100)

for c, n in enumerate(nuns):
    print(f'Na posição {c} encontrei o valor {n}.')


print('='*100)
print('Agora é a sua vez de tentar!')
prog = list()
for c in range(0,5):
    prog.append(int(input('Digite um valor: '))) #vai solicitar um valor 5 vezes que definirá os números da variável prog
print('='*100)
for p, n in enumerate(prog):
    print(f'Na posição {p} encontrei o valor {n}.')
print('='*100)
