from idlelib.mainmenu import menudefs


def Cadastro():
    print("Realize seu cadastro!")
    email = input("Digite seu email: ")
    senha = input("Digite uma senha: ")
    loc = input("Digite sua cidade: ")
    print("Cadastro feito com sucesso!")
    Menu()
def Menu():
    while True:
        choose = int(input("O que deseja Realizar? \n 1 - Receber dicas em caso de enchente \n 2 - Verificar a probabilidade de chuva \n 3 - Verificar o nivel de agua e probabilidade de enchente \n 4 - Encerrar sistema"))
        match choose:
            case 1:
                Dicas()
            case 2:
                Probabilidade()
            case 3:
                Nivel()
            case 4:
                break
            case _:
                print("Opcao invalida escolha outra opcao")

def Dicas():
    print("Vou colocar depois")

def Probabilidade():
    temp = float(input("Digite o temperatura em Celsius: "))
    umid = float(input("Digite a umidade do ar em %: "))
    vent = float(input("Digite a velocidade do vento em km/h: "))

    if temp < 18:
        temp = 0
    elif temp > 30:
        temp = 24
    else:
        temp = (temp - 18) * 2

    if vent < 5:
        vent = 0
    elif vent > 20:
        vent = 30
    else:
        vent = (vent - 5) * 2

    probabilidade = (0.6 * umid) + (0.3 * temp) + (0.1 * vent)
    print(f"Probabilidade de chuva: {probabilidade}")

def Nivel():
    estado = int(input("Esta chovendo no momento? \n 1 - Sim  \n 2 - Nao"))
    if estado == 1:
        estado = int(input("Qual o nivel da chuva? \n 1 - Chuva fraca \n 2 - Chuva moderada \n 3 - Chuva forte"))
        if estado == 1:
            print("Analisando o nivel da agua do esgoto e rios proximos a sua localizacao a chance de enchente e proxima de 0%")
        if estado == 2:
            print("Analisando o nivel da agua do esgoto e rios proximos a sua localizacao a chance de enchente e aproximadamente 23%")
        if estado == 3:
            print("Analisando o nivel da agua do esgoto e rios proximos a sua localizacao a chance de enchente e aproximadamente 60%, fique atento")
    if estado == 2:
        print("Nao a risco de enchentes no momento")
Cadastro()