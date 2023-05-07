def boasVindas(nome):
    print("---------------------------------------------------------------------")
    print("Seja bem vindo(a) ao novo app de otimização para ônibus!"
          "\nNosso app é muito simples, consiste em mostrar com eficiência quais ônibus podem te levar ao seu destino!")
    print(f"Ok {nome}, muito obrigado por baixar nosso aplicativo")

def mostrarDestino(destino, lista):
    print(f"Os ônibus disponíveis para o endereço {destino} são: ")
    for nome in lista:
        print(nome)
    print("Obrigado por usar nosso app!")

