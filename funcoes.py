def boasVindas(nome):
    print("---------------------------------------------------------------------")
    print("Seja bem vindo(a) ao novo app de otimização para ônibus!"
          "\nNosso app é muito simples, consiste em mostrar com eficiência quais ônibus podem te levar ao seu destino!")
    print(f"Ok {nome}, muito obrigado por baixar nosso aplicativo")

def mostrarDestino1(destino):
    print(f"Os ônibus disponíveis para o endereço {destino} são: "
          f"\n477A - Term. PINHEIROS - Lotação: 3.0 - Tempo de chegada: 10 minutos!"
          f"\n5142 - Term. PQ DOM PEDRO II - Lotação: 4.5 - Tempo de chegada: 7 minutos!"
          f"\n476G - IBIRAPUERA - Lotação: 2.5 - Tempo de chegada: 15 minutos!"
          f"\n3390 - Term. PQ DOM PEDRO II - Lotação: 3.5 - Tempo de chegada: 13 minutos!")
    print("Obrigado por usar nosso app!")

def mostrarDestino2(destino):
    print(f"Os ônibus disponíveis para o endereço {destino} são: "
          f"\n476G - IBIRAPUERA - Lotação: 2.5 - Tempo de chegada: 15 minutos!"
          f"\n4115 - PRAÇA DA REPÚBLICA - Lotação: 5.0 - Tempo de chegada: 18 minutos!"
          f"\n407M - METRÔ VILA MARIANA - Lotação: 3.5 - Tempo de chegada: 10 minutos!"
          f"\n5705 - METRÔ VERGUEIRO - Lotação: 1.5 - Tempo de chegada: 8 minutos!")
    print("Obrigado por usar nosso app!")

def mostrarDestino3(destino):
    print(f"Os ônibus disponíveis para o endereço {destino} são: "
          f"\n874T - LAPA - Lotação: 4.0 - Tempo de chegada: 5 minutos!"
          f"\n975A - VILA BRASILÂNDIA - Lotação: 5.0 - Tempo de chegada: 7 minutos!"
          f"\n407M - METRÔ VILA MARIANA - Lotação: 3.5 - Tempo de chegada: 10 minutos!"
          f"\n3390 - Term. PQ DOM PEDRO II - Lotação: 3.5 - Tempo de chegada: 13 minutos!")
    print("Obrigado por usar nosso app!")

def perguntarDestino(destinos):
    destino = input(f"Para qual destino você gostaria de ir?"
                    f"\nDigite 1 para {destinos[0]}"
                    f"\nDigite 2 para {destinos[1]}"
                    f"\nDigite 3 para {destinos[2]}\n")
