print('='*100)
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[2][0]) #vai aparecer a váriavel 0 dentro da variável 2
print(pessoas[1]) #vai aparecer a váriavel 1 inteira
print('='*100)

#teste
teste = list()
teste.append('Maria')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0]  = 'Karen'
teste [1] = 20
galera.append(teste[:])
print(galera)
print('='*100)

#teste2
galeris = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeris[0][0])
print(galeris[0][1])
print(galeris[3][1])
for p in galeris:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('='*100)

#teste3
totmai = totmen = 0
gal = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

for p in gal:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Ao todo, temos {totmai} maiores e {totmen} menores de idade.')
       