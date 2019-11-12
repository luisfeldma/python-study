inputs = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')))
print(f'Você digitou os valores: {inputs}')
print(f'Você digitou o número nove {inputs.count(9)} vezes.')
quant = 0
for n in inputs:
    if n % 2 == 0:
        quant += 1
print(f'Você digitou {quant} números pares.')        
        