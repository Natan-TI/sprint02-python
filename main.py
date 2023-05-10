from funcoes import *
destinos = ["Av. Lins de Vasconcelos, 1222 (FIAP)", "Estação Vila Mariana", "Avenida Paulista, 1578 (MASP)"]
onibus_destino01 = ["477A - Term. PINHEIROS - Lotação: 3.0 - Tempo de chegada: 10 minutos!",
                   "5142 - Term. PQ DOM PEDRO II - Lotação: 4.5 - Tempo de chegada: 7 minutos!",
                   "476G - IBIRAPUERA - Lotação: 2.5 - Tempo de chegada: 15 minutos!",
                   "3390 - Term. PQ DOM PEDRO II - Lotação: 3.5 - Tempo de chegada: 13 minutos!"]

onibus_destino02 = ["476G - IBIRAPUERA - Lotação: 2.5 - Tempo de chegada: 15 minutos!",
                   "4115 - PRAÇA DA REPÚBLICA - Lotação: 5.0 - Tempo de chegada: 18 minutos!",
                   "407M - METRÔ VILA MARIANA - Lotação: 3.5 - Tempo de chegada: 10 minutos!",
                   "5705 - METRÔ VERGUEIRO - Lotação: 1.5 - Tempo de chegada: 8 minutos!"]

onibus_destino03 = ["874T - LAPA - Lotação: 4.0 - Tempo de chegada: 5 minutos!",
                   "975A - VILA BRASILÂNDIA - Lotação: 5.0 - Tempo de chegada: 7 minutos!",
                   "407M - METRÔ VILA MARIANA - Lotação: 3.5 - Tempo de chegada: 10 minutos!",
                   "3390 - Term. PQ DOM PEDRO II - Lotação: 3.5 - Tempo de chegada: 13 minutos!"]
frase = f"Para qual destino você gostaria de ir?\nDigite 1 para {destinos[0]}\nDigite 2 para {destinos[1]}\nDigite 3 para {destinos[2]}\n"
frase2 = f"Você precisa digitar 1, 2 ou 3!\nPara qual destino você gostaria de ir?\nDigite 1 para {destinos[0]}\nDigite 2 para {destinos[1]}\nDigite 3 para {destinos[2]}\n"
print("---------------------------------------------------------------------")
nome = input("Qual é o seu nome? ")
boas_vindas(nome)
resposta = obrigar_usuario("Você gostaria de testar a otimização na busca por transportes públicos? (s/n) ", 'S', 'N')
while resposta == 'S':
    destino = teste_numerico(frase, frase2)
    if destino == 1:
        mostrar_destino(destinos[0], onibus_destino01)
    elif destino == 2:
        mostrar_destino(destinos[1], onibus_destino02)
    elif destino == 3:
        mostrar_destino(destinos[2], onibus_destino03)
    else:
        print("Destino não disponível no momento...")
    resposta = obrigar_usuario("Você gostaria de testar novamente? (s/n) ", 'S', 'N')
else:
    print(f"Tenha um bom dia {nome}!")