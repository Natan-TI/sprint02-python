def boasVindas(nome):
    print("---------------------------------------------------------------------")
    print("Seja bem vindo(a) ao novo app de otimização para ônibus!"
          "\nNosso app é muito simples, consiste em mostrar com eficiência quais ônibus podem te levar ao seu destino!")
    print(f"Ok {nome}, muito obrigado por baixar nosso aplicativo")

def mostrarDestino1(destino, lista):
    print(f"Os ônibus disponíveis para o endereço {destino} são: ")
    for nome in lista:
        print(nome)
    print("Obrigado por usar nosso app!")

def mostrarDestino2(destino, lista):
    print(f"Os ônibus disponíveis para o endereço {destino} são: ")
    for nome in lista:
        print(nome)
    print("Obrigado por usar nosso app!")

def mostrarDestino3(destino, lista):
    print(f"Os ônibus disponíveis para o endereço {destino} são: ")
    for nome in lista:
        print(nome)
    print("Obrigado por usar nosso app!")

def perguntarDestino(destinos):
    destino = input(f"Para qual destino você gostaria de ir?"
                    f"\nDigite 1 para {destinos[0]}"
                    f"\nDigite 2 para {destinos[1]}"
                    f"\nDigite 3 para {destinos[2]}\n")
