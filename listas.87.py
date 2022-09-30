matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = col = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('='*100)
for l in range(0,3):
    for c in range(0,3):
       print(f'[{matriz[l][c]:^5}]', end='')
       if matriz[l][c] % 2 == 0:
        par += matriz[l][c]
    print()
print('='*100)

#a)
print(f'A soma de todos os números pares digitados é de {par}.')

#b)
for l in range(0,3):
    col += matriz[l][2]
print(f'A soma dos valores da terceira coluna é de {col}.')

#c)
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')