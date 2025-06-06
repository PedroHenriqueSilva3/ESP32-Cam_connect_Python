import asyncio  # Pode ser útil para futuras funcionalidades assíncronas
# from idlelib.mainmenu import menudefs  # Removido: não é necessário para este código

def cadastro():
    """
    Realiza o cadastro do usuário, solicitando e-mail, senha e cidade com validação.
    """
    print("Realize seu cadastro!")

    while True:
        email = input("Digite seu e-mail: ").strip()
        if email:
            break
        else:
            print("O e-mail não pode estar em branco.")

    # Confirmação de senha com verificação
    while True:
        senha = input("Digite sua senha: ").strip()
        senha1 = input("Confirme sua senha: ").strip()

        if not senha or not senha1:
            print("A senha não pode estar em branco.")
        elif senha != senha1:
            print("As senhas são diferentes. Tente novamente.")
        else:
            break

    while True:
        cidade = input("Digite sua cidade: ").strip()
        if cidade:
            break
        else:
            print("A cidade não pode estar em branco.")

    print("Cadastro feito com sucesso!\n")
    menu()


def login():
    """
    Realiza o login do usuário com validação de entrada.
    """
    while True:
        email = input("Digite seu e-mail: ").strip()
        if email:
            break
        else:
            print("O e-mail não pode estar em branco.")

    while True:
        senha = input("Digite sua senha: ").strip()
        if senha:
            break
        else:
            print("A senha não pode estar em branco.")

    print("Login feito com sucesso!\n")
    menu()


def menu():
    """
    Apresenta o menu principal com opções funcionais.
    """
    while True:
        print("\nO que deseja realizar?")
        print("1 - Receber dicas em caso de enchente")
        print("2 - Verificar a probabilidade de chuva")
        print("3 - Verificar o nível de água e probabilidade de enchente")
        print("4 - Encerrar sistema")

        escolha = input("Digite a opção desejada: ")

        match escolha:
            case "1":
                dicas()
            case "2":
                try:
                    temp = float(input("Digite a temperatura em Celsius: "))
                    umid = float(input("Digite a umidade do ar em %: "))
                    vent = float(input("Digite a velocidade do vento em km/h: "))
                    prob = probabilidade(temp, umid, vent)
                    print(f"Com base nas informações, a probabilidade de chuva é de: {prob:.1f}%\n")
                except ValueError:
                    print("Erro: insira apenas valores numéricos válidos para temperatura, umidade e vento.\n")
            case "3":
                nivel()
            case "4":
                print("Sistema encerrado.")
                break
            case _:
                print("Opção inválida. Escolha outra opção.\n")

def dicas():
    """
    Apresenta dicas de segurança em caso de enchente.
    """
    print("⚠️ Em caso de enchente:")
    print("- Evite contato com a água da enchente.")
    print("- Desligue aparelhos elétricos e mantenha-se em local seguro e elevado.")
    print("- Acompanhe boletins da Defesa Civil e prefeituras locais.\n")

def probabilidade(t, u, v):
    """
    Calcula a probabilidade de chuva com base na temperatura (t),
    umidade relativa do ar (u) e velocidade do vento (v).
    """
    # Ajuste da temperatura
    if t < 18:
        t = 0
    elif t > 30:
        t = 24
    else:
        t = (t - 18) * 2

    # Ajuste da velocidade do vento
    if v < 5:
        v = 0
    elif v > 20:
        v = 30
    else:
        v = (v - 5) * 2

    # Cálculo da probabilidade
    return (0.6 * u) + (0.3 * t) + (0.1 * v)

def nivel():
    """
    Simula risco de enchente utilizando nível da água (utilizando sensores com arduino) e intesidade de chuva no momento. (valores fictícios)
    """
    try:
        estado = int(input("Está chovendo no momento? \n1 - Sim\n2 - Não\nDigite: "))
        if estado == 1:
            intensidade = int(input("Qual o nível da chuva?\n1 - Chuva fraca\n2 - Chuva moderada\n3 - Chuva forte\nDigite: "))
            match intensidade:
                case 1:
                    print("Chance de enchente próxima de 0%.\n")
                case 2:
                    print("Chance de enchente aproximadamente 23%.\n")
                case 3:
                    print("Chance de enchente aproximadamente 60%. Fique atento!\n")
                case _:
                    print("Opção inválida para nível de chuva.\n")
        elif estado == 2:
            print("Não há risco de enchentes no momento.\n")
        else:
            print("Opção inválida.\n")
    except ValueError:
        print("Erro: insira apenas números inteiros válidos.\n")

def inicio():
    """
    Inicia o sistema oferecendo opções de cadastro ou login.
    """
    while True:
        try:
            escolha = int(input("1 - Cadastrar-se\n2 - Login\nDigite: "))
            if escolha == 1:
                cadastro()
                break
            elif escolha == 2:
                login()
                break
            else:
                print("Opção inválida. Escolha outra opção.")
        except ValueError:
            print("Erro: digite apenas 1 ou 2.")

# Execução principal
inicio()
