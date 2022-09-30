#usando o sort
nun = []
maior = menor = 0

print('='*100)
for c in range(0,5):
    nun.append(int(input(f'Digite um número para a posição {c}: ')))
nun.sort()
print(f'Os seus números escolhidos, ordem crescente, ficam como: {nun}.')
print('='*100)


#sem usar o sort
list = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem crescente foram: {list}.')
print('='*100)