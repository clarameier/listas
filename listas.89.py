ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Avaliação 1: '))
    nota2 = float(input('Avaliação 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja adicionar mais alunos e suas notas? [S/N]: '))
    if resp in 'Nn':
        break
print('='*100)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('='*100)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*100)
    opc = int(input('Deseja ver as notas de qual aluna(o)? (999 interrompe) '))
    if opc == 999:
        print('finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('='*100)