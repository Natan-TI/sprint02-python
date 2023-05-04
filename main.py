from funcoes import *
destinos = ["Av. Lins de Vasconcelos, 1222 (FIAP)", "Estação Vila Mariana", "Avenida Paulista, 1578 (MASP)"]
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
        mostrarDestino1(destinos[0])
    elif destino == 2:
        mostrarDestino2(destinos[1])
    elif destino == 3:
        mostrarDestino3(destinos[2])
    else:
        print("Destino não disponível no momento...")
    resposta = input("Você gostaria de testar novamente? (s/n) ").upper()
    while resposta != 'S' and resposta != 'N':
        print("Você precisa digitar \'s\' ou \'n\'!")
        resposta = input("Você gostaria de testar novamente? (s/n) ").upper()
else:
    print(f"Tenha um bom dia {nome}!")