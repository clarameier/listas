nun = [2, 5, 9, 1] #precisa deixar em [] para conseguir alterar a tupla, se deixar em () vai dar erro
nun[2] = 3
nun.append(7) #append é para adicionar um último valor no final da tupla
nun.sort() #deixa os valores da tupla em ordem crescente
nun.sort(reverse=True) #deixa os valores da tupla em ordem decrescente
nun.insert(2, 0) #adiciona um número 0 (ou o que eu escolher) na posição 2 (ou o que eu escolher)
nun.pop() #elimina o último valor da tupla
nun.pop(2) #elimina o valor da posição 2 (ou a que eu escolher)
nun.remove(7) #elimina o valor 7 (ou o que eu escolher)
if 4 in nun:  #se houver na tupla, remove o número 4 (ou o que eu escolher), senão, não remove e aparece mensagem de que não há o número escolhido
    nun.remove(4)
else:
    print('Não achei o número 4!')
print(nun)
print(f'Essa lista da tupla tem {len(nun)} números') #lê a quantidade de números informados