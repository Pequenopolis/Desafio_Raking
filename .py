Nome_Herói = input("Qual o nome do seu Herói? ")
Batalhas_Vitorias = 100
Batalhas_Derrotas = 0
#Saldo_de_Batalhas = Batalhas_Vitorias - Batalhas_Derrotas
Ranking = {
10:"Ferro",
20:"Bronze",
50:"Prata",
80:"Ouro",
90:"Diamante",
100:"Lendario"
}

def calcular_classificacao(vitorias, derrotas):
   saldo_de_batalhas = vitorias - derrotas
   classificacao = None
   for saldo, nome in Ranking.items():
    if saldo_de_batalhas <= saldo:
       classificacao = nome
       break
   return classificacao

classificacao = calcular_classificacao(Batalhas_Vitorias, Batalhas_Derrotas)
if classificacao:
   print(f'O ranking do Herói {Nome_Herói} é {classificacao}')
else:
   print(f'O ranking do Herói {Nome_Herói} é Radiante')

# if Saldo_de_Batalhas <= 10:
#    print(f'O ranking do Herói {Nome_Herói} é Ferro')
# elif Saldo_de_Batalhas > 10 and Saldo_de_Batalhas <= 20:
#    print(f'O ranking do Herói {Nome_Herói} é Bronze')
# elif Saldo_de_Batalhas > 20 and Saldo_de_Batalhas <= 50:
#    print(f'O ranking do Herói {Nome_Herói} é Prata')
# elif Saldo_de_Batalhas > 50 and Saldo_de_Batalhas <= 80:
#    print(f'O ranking do Herói {Nome_Herói} é Ouro')
# elif Saldo_de_Batalhas > 80 and Saldo_de_Batalhas <= 90:
#    print(f'O ranking do Herói {Nome_Herói} é Diamante')
# elif Saldo_de_Batalhas > 90 and Saldo_de_Batalhas <= 100:
#    print(f'O ranking do Herói {Nome_Herói} é Lendario') 
# else:
#    print(f'O ranking do Herói {Nome_Herói} é Radiante')
#def Função_de_Calssificacao_do_Ranking():
