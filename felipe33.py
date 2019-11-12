n = int(input("Digite um número entre 0 a 10: "))
while n > 10 or n < 0:
    n = int(input("Digite um número ENTRE 0 e 10: "))
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
print(f'Você digitou o número {lista[n]}.')    