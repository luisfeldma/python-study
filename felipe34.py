tabela = ('City', 'Liverpool', 'Tottenham', 'Arsenal', 'Manchester United', 'Chelsea', 'Wolves', 'Watford', 'West Ham', 'Leicester City')
print(f'Os três primeiros colocados são: {tabela[:3]}.')
print(f'Os dois ultimos colocados são: {tabela[-2:]}.')
print(f'Times em ordem alfabetica: {sorted(tabela)}.')
print(f'O City está na {tabela.index("City") + 1} posição.')