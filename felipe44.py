expressao = str(input('Digite uma expressão: '))
pilha = []
for símbolo in expressao:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')    
if len(pilha) > 0:
    print('Sua expressão está inválida.')
else:
    print('Sua expressão é válida.')    
