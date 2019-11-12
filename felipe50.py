infos = list()
while True:
    nome = str(input('Nome: ')).title().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    infos.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-------------------------')
for i, a in enumerate(infos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Deseja mostras as notas de qual aluno? [999 interrompe]: '))   
    if opc == 999:
        break
    if opc <= len(infos):
        print(f'As notas de {infos[opc][0]} são: {infos[opc][1]} ')     
       