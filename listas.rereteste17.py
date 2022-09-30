a = [2, 3, 4, 7]
b = a[:] #cria uma cópia sem fazer ligação direta
b[2] = 8 #altera o valor da posição 2 pelo número 8 (ou o que eu escolher)

print(f'Lista A: {a}')
print(f'Lista B: {b}')