jogador = dict()
gols = list()
jogador['Nome'] = str(input('Jogador: ')).strip().title()
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Partidas'] = tot
for c in range(1, tot + 1):
    gols.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['Gols'] = gols[:]    
jogador['Total'] = sum(gols)
print(f'''O jogador {jogador['Nome']} possui uma média de {(jogador['Total'] / tot)} gols por jogo.
''') 
