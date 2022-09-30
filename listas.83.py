from turtle import st


conta = str(input('Digite uma expressão qualquer: '))
verif = []
for simb in conta:
    if simb == '(':
        verif.append('(')
    elif simb == ')':
        if len(verif) > 0:
            verif.pop()
        else:
            verif.append(')')
            break
if len(verif) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')