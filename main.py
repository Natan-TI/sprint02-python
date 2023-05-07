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
print("---------------------------------------------------------------------")
nome = input("Qual é o seu nome? ")
boasVindas(nome)
resposta = input("Você gostaria de testar a otimização na busca por transportes públicos? (s/n) ").upper()
while resposta != 'S' and resposta != 'N':
    print("Você precisa digitar \'s\' ou \'n\'!")
    resposta = input("Você gostaria de testar a otimização na busca por transportes públicos? (s/n) ").upper()
while resposta == "S":
    destino = input(f"Para qual destino você gostaria de ir?"
                    f"\nDigite 1 para {destinos[0]}"
                    f"\nDigite 2 para {destinos[1]}"
                    f"\nDigite 3 para {destinos[2]}\n")
    while not destino.isnumeric():
        print("Você precisa digitar 1, 2 ou 3!")
        destino = input(f"Para qual destino você gostaria de ir?"
                        f"\nDigite 1 para {destinos[0]}"
                        f"\nDigite 2 para {destinos[1]}"
                        f"\nDigite 3 para {destinos[2]}\n")
    destino = int(destino)
    if destino == 1:
        mostrarDestino(destinos[0], onibus_destino01)
    elif destino == 2:
        mostrarDestino(destinos[1], onibus_destino02)
    elif destino == 3:
        mostrarDestino(destinos[2], onibus_destino03)
    else:
        print("Destino não disponível no momento...")
    resposta = input("Você gostaria de testar novamente? (s/n) ").upper()
    while resposta != 'S' and resposta != 'N':
        print("Você precisa digitar \'s\' ou \'n\'!")
        resposta = input("Você gostaria de testar novamente? (s/n) ").upper()
else:
    print(f"Tenha um bom dia {nome}!")