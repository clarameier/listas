valist = [[], []]
valor = 0
for c in range(1,8):
   valor = int(input(f'Digite um valor na {c}° posição: '))
   if valor % 2 == 0:
        valist[0].append(valor)
   else:
        valist[1].append(valor)
print('='*100)

valist[0].sort()
valist[1].sort()

print(f'Estes números {valist[0]} são pares.')
print(f'Estes números {valist[1]} são pares.')