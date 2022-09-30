print('='*100)
tela = []
maior = 0
menor = 0

for c in range(0,5):
    tela.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = tela[c]
    else:
        if tela[c] > maior:
            maior = tela[c]
        if tela[c] < menor:
            menor = tela[c]
print('='*100)

print(f'O maior número digitado por você foi {maior} e ele está na posição ', end='')
for ind, val in enumerate(tela):
    if val == maior:
        print(f'{ind}... ', end='')
print()
print('='*100)

print(f'O menor número digitado por você foi {menor} e ele está na posição ', end='')
for ind, val in enumerate(tela):
    if val == menor:
        print(f'{ind}... ', end='')
print()
print('='*100)