def boas_vindas(nome):
    print("---------------------------------------------------------------------")
    print("Seja bem vindo(a) ao novo app de otimização para ônibus!"
          "\nNosso app é muito simples, consiste em mostrar com eficiência quais ônibus podem te levar ao seu destino!")
    print(f"Ok {nome}, muito obrigado por baixar nosso aplicativo")


def mostrar_destino(destino, lista):
    print(f"Os ônibus disponíveis para o endereço {destino} são: ")
    for nome in lista:
        print(nome)
    print("Obrigado por usar nosso app!")


def obrigar_usuario(frase, arg1, arg2):
    resposta = input(frase).upper()
    while resposta != arg1 and resposta != arg2:
        print(f"Você precisa digitar \'{arg1}\' ou \'{arg2}\'!")
        resposta = input(frase).upper()
    return resposta


def teste_numerico(frase, frase2):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase2)
    var = int(var)
    return var
