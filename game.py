import random
import time

# Constantes
VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
MOCHILA_LIMITE = 5

# Variáveis do jogador
vida = VIDA_MAXIMA
energia = ENERGIA_MAXIMA
pontuacao = 0
mochila = []
noites = []
interacoes_animais = {
    "javali": False,
    "veado": False,
    "coruja": False
}
lugares_visitados = {
    "abrigo": False,
    "fonte": False,
    "topo da árvore": False,
    "trilha": False,
    "clareira": False,
    "casa": False
}


# Funções do jogo
def introducao():
    print("=" * 50)
    print("🌲 JOGO DE AVENTURA - FUJA DA FLORESTA 🌲")
    print("=" * 50)
    print("\nVocê acorda no meio de uma floresta desconhecida.")
    print("Seu objetivo é sobreviver até encontrar o caminho de volta para casa.")
    print("\nRegras do jogo:")
    print("- Tome decisões que afetam seu destino.")
    print("- A cada escolha, você pode ganhar ou perder pontos.")
    print("- Animais selvagens, fome e clima são seus inimigos.")
    print("- Colete recursos, evite perigos e tente escapar com vida!\n")
    print("- Ganha ao atingir 100 pontos ou morre se a vida ou energia chegarem a zero.")
    print("\nBoa sorte, aventureiro!\n")
    input("Pressione ENTER para começar sua jornada...\n")

def verificar_game_over():
    if vida <= 0 or energia <= 0:
        print("\n💀 Você não resistiu... Fim de jogo.")
        exit()
def verificar_vitoria():
    if pontuacao >= 100:
        print("\n🏆 PARABÉNS! Você acumulou 100 pontos e conseguiu sair da floresta com sucesso!")
        print("Obrigado por jogar!\n")
        exit()

def mostrar_status():
    print("\n📊 STATUS ATUAL:")
    print(f"Vida: {vida}/{VIDA_MAXIMA}")
    print(f"Energia: {energia}/{ENERGIA_MAXIMA}")
    print(f"Pontuação: {pontuacao}\n")

def ver_mochila():
    global vida, energia, mochila

    while True:
        print("\n🎒 ITENS NA MOCHILA:")
        if mochila:
            for i, item in enumerate(mochila, 1):
                print(f"{i}. {item}")
            print("0. Voltar")

            escolha = input("Digite o número do item para usá-lo ou 0 para voltar: ")
            
            if escolha == "0":
                break

            try:
                indice = int(escolha) - 1
                item = mochila[indice]

                if "Frutas" in item:
                    energia = min(ENERGIA_MAXIMA, energia + 10)
                    vida = min(VIDA_MAXIMA, vida + 10)
                    print("🍎 Você comeu frutas. +10 de vida, +10 de energia.")
                elif "Ervas" in item:
                    vida = min(VIDA_MAXIMA, vida + 20)
                    print("🌿 Você usou ervas medicinais. +20 de vida.")
                elif "Mapa" in item:
                    energia -= 15
                    print("📜 Você estuda o mapa, mas apenas te fez perder tempo. -15 de energia")
                elif "Carne" in item:
                    energia = min(ENERGIA_MAXIMA, energia + 20)
                    vida = min(VIDA_MAXIMA, vida + 20)
                    print("🥩 Você comeu carne. +20 de energia, +20 de vida")
                elif "Frutas Brilhantes" in item:
                    energia = min(ENERGIA_MAXIMA, energia + 15)
                    vida = min(VIDA_MAXIMA, vida + 15)
                    print("🌟 Você comeu frutas brilhantes. +15 de energia, +15 de vida.")
                          
                 
                mochila.pop(indice)
                verificar_game_over() 
                verificar_vitoria()    
                break

            except (IndexError, ValueError):
                print("Entrada inválida. Escolha um número válido.")
        else:
            print("Sua mochila está vazia.")
            break

def ver_noites():
    print("\n🏅 Noites na Floresta:")
    if noites:
        for i, noite in enumerate(noites, 1):
            print(f"{i}. {noite}")
    else:
        print("Você ainda não passou nenhuma noite na floresta.")


def primeira_escolha():
    global vida, energia, pontuacao, mochila

    print("Você está cercado por árvores altas e ouve sons estranhos ao longe.")
    print("O que deseja fazer?\n")
    print("(1) Buscar comida")
    print("(2) Montar abrigo")
    print("(3) Explorar a floresta")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🍎 Depois de um tempo procurando você finalmente encontrou frutas silvestres.-10 de energia (+1 item na mochila)")
            pontuacao += 10
            energia -= 10
            if len(mochila) < MOCHILA_LIMITE:
                mochila.append("Frutas Silvestres")
            else:
                print("Mochila cheia! Não foi possível guardar as frutas.")
            break

        elif escolha == "2":
            print("\n🪓 Você montou um abrigo. +15 pontos, -15 de energia.")
            pontuacao += 15
            energia -= 15
            lugares_visitados["abrigo"] = True
            break

        elif escolha == "3":
            print("\n🐾 Você saiu para explorar... encontrou pegadas de um animal grande!")
            print("Sem abrigo e sem comida: -15 de vida, -20 de energia, -5 pontos.")
            vida -= 15
            energia -= 20
            pontuacao -= 5
            break

        else:
            print("\nOpção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def segunda_escolha():
    global vida, energia, pontuacao, mochila

    print("Você descansou um pouco e está pronto para ver seus status e continuar sua jornada.")
    print("Qual será sua próxima ação?\n")
    print("(1) Seguir por uma trilha misteriosa")
    print("(2) Procurar uma fonte de água")
    print("(3) Subir em uma árvore para tentar se orientar")
    print("(4) Ver mochila")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n📜 A trilha leva a uma parte escura da floresta. Você encontra um mapa velho! -15 de energia +15 pontos. (+1 item na mochila)")
            pontuacao += 15
            energia -= 15
            lugares_visitados["trilha"] = True
            if len(mochila) < MOCHILA_LIMITE:
                mochila.append("Mapa")
            else:
                print("Mochila cheia! Não foi possível guardar o mapa.")
            break

        elif escolha == "2":
            print("\n💧 Você encontra uma pequena nascente! +10 de energia, +10 pontos.")
            energia = min(ENERGIA_MAXIMA, energia + 10)
            pontuacao += 10
            lugares_visitados
            break

        elif escolha == "3":
            print("\n🌳 Você sobe numa árvore alta. Consegue ver uma possível saída ao norte! +5 pontos, -10 de energia.")
            energia -= 10
            pontuacao += 5
            lugares_visitados["topo da árvore"] = True
            break
        elif escolha == "4":
            ver_mochila()

        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def terceira_escolha():
    global vida, energia, pontuacao

    print("Você está andando silenciosamente pela floresta quando ouve um barulho nos arbustos...")
    time.sleep(4)
    print("Você para. O som está cada vez mais perto...")
    time.sleep(6)
    print("É um animal selvagem!\n")

    evento = random.choice(["ataque", "fuga", "neutro"])

    if evento == "ataque":
        print("🐗 Um javali bravo te ataca! Você se machuca ao fugir. -20 de vida, -15 de energia e -10 pontos")
        vida -= 20
        energia -= 15
        pontuacao -= 10
        interacoes_animais["javali"] = True

    elif evento == "fuga":
        print("🦌 Era um veado assustado. Ele corre e você se esconde, e aproveita para descansar um pouco. +10 de energia")
        energia = min(ENERGIA_MAXIMA, energia + 10)
        interacoes_animais["veado"] = True

    else:
        print("🦉 É apenas uma coruja que estava caçando. Ufa! Nada acontece.")
        interacoes_animais["coruja"] = True

    
    
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def quarta_escolha():
    global vida, energia, pontuacao, mochila

    print("Você encontra uma clareira iluminada pelo sol.")
    lugares_visitados["clareira"] = True
    print("O que deseja fazer?\n")
    print("(1) Construir uma fogueira")
    print("(2) Tentar fazer um sinal de socorro")
    print("(3) Explorar a clareira em busca de recursos")
    print("(4) Ver mochila")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🔥 Você constrói uma fogueira. +10 pontos, -15 de energia.")
            pontuacao += 10
            energia -= 15
            break

        elif escolha == "2":
            print("\n🚨 Você faz um sinal de socorro com galhos e folhas. +20 pontos, -10 de energia.")
            pontuacao += 20
            energia -= 10
            break

        elif escolha == "3":
            print("\n🌿 Você encontra ervas medicinais! +15 pontos, -5 energia. (+1 item na mochila)")
            pontuacao += 15
            energia -= 5
            if len(mochila) < MOCHILA_LIMITE:
                mochila.append("Ervas Medicinais")
            else:
                print("Mochila cheia! Não foi possível guardar as ervas.")
            break

        elif escolha == "4":
            ver_mochila()

        else:
            print("\nOpção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def quinta_escolha():
    global vida, energia, pontuacao, mochila

    print("Está escurecendo e você está perdido, não se lembra mais de onde veio. Precisa decidir o que fazer a seguir.")
    print("Você tem algumas opções:\n")
    print("(1) Passar a noite na clareira")
    print("(2) Tenta fazer algo para se defender de animais noturnos")
    print("(3) Tentar encontrar o caminho de volta para a trilha")
    print("(4) Ver mochila")
    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🌙 Você passa a noite na clareira. +10 pontos, +20 de energia.")
            pontuacao += 10
            energia += 20
            verificar_game_over()
            verificar_vitoria()
            break

        elif escolha == "2":
            print("\n 🏹 Você conseguiu construir uma armadilha, e consegue 🥩 carne. +15 pontos, -10 de energia. (+ 1 item na mochila)")
            pontuacao += 15
            energia -= 10
            if len(mochila) < MOCHILA_LIMITE:
                mochila.append("Carne")
            else:
                print("Mochila cheia! Não foi possível guardar o arco e a carne.")
            verificar_game_over()
            verificar_vitoria()
            break

        elif escolha == "3":
            print("\n🧭 Você tenta encontrar o caminho de volta, mas acaba se perdendo mais. -10 pontos, -30 de energia.")
            pontuacao -= 10
            energia -= 30
            verificar_game_over()
            verificar_vitoria()
            break

        elif escolha == "4":
            ver_mochila()

        else:
            print("\nOpção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")


def sexta_escolha():
    global vida, energia, pontuacao, mochila, noites
    noites.append("Noite na floresta")
    print("🌅 O sol começa a nascer no horizonte.")
    print("Depois de uma noite difícil, você sente uma leve esperança no ar.")
    print("É hora de decidir como começar o novo dia.\n")
    print("(1) Seguir em direção ao sol em busca de uma possível saída")
    print("(2) Procurar mais recursos antes de continuar")
    print("(3) Descansar mais um pouco para recuperar energia")
    print("(4) Ver mochila")
    print("(5) Ver noites passadas")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🧭 Você segue rumo ao norte com coragem.")
            print("Após caminhar por horas, começa a ver sinais de civilização!")
            pontuacao += 25
            energia -= 15
            print("+25 pontos, -15 de energia.")
            break

        elif escolha == "2":
            print("\n🍄 Você decide explorar ao redor.")
            evento = random.choice(["encontrou frutas", "nada encontrado", "feriu o pé"])
            if evento == "encontrou frutas":
                print("Você achou algumas frutas exóticas! +10 pontos, (+1 item na mochila)")
                pontuacao += 10
                if len(mochila) < MOCHILA_LIMITE:
                    mochila.append("Frutas Silvestres")
                else:
                    print("Mochila cheia! Não foi possível guardar as frutas.")
            elif evento == "nada encontrado":
                print("Você procurou por um tempo, e encontrou apenas rastros que você mesmo deixou. -10 de energia.")
                energia -= 10
            else:
                print("Você escorregou e feriu o pé. -10 de vida, -10 de energia.")
                vida -= 10
                energia -= 10
            break

        elif escolha == "3":
            print("\n😴 Você decide descansar mais um pouco sob o sol da manhã.")
            energia = min(ENERGIA_MAXIMA, energia + 20)
            vida = min(VIDA_MAXIMA, vida + 10)
            print("+20 de energia, +10 de vida.")
            break

        elif escolha == "4":
            ver_mochila()

        elif escolha == "5":
            ver_noites()

        else:
            print("\nOpção inválida. Por favor, escolha uma das opções.")

    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def setima_escolha():
    global vida, energia, pontuacao, mochila

    print("Você finalmente encontra uma pequena estrada de terra.")
    print("Ao longe, vê uma casa abandonada. O que deseja fazer?\n")
    print("(1) Entrar na casa em busca de ajuda")
    print("(2) Continuar pela estrada")
    print("(3) Ver mochila")
    print("(4) Ver noites passadas")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🏠 Você entra na casa e aproveita para descansar em segurança! +30 pontos, +20 de energia.")
            pontuacao += 30
            energia += 20
            lugares_visitados["casa"] = True
            break

        elif escolha == "2":
            print("\n🚶 Você decide continuar pela estrada. +10 pontos, -10 de energia.")
            pontuacao += 10
            energia -= 10
            break

        elif escolha == "3":
            ver_mochila()
        
        elif escolha == "4":
            ver_noites()

        else:
            print("\nOpção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")

def oitava_escolha():
    global vida, energia, pontuacao, mochila

    print("Quando está tudo dando certo, você ouve um barulho de algum animal.")
    print("Você se esconde o barulho está cada vez mais próximo.")
    time.sleep(4)
    print("É um animal selvagem!\n")
    print("Você tem algumas opções:\n")
    print("(1) Continuar se escondendo")
    print("(2) Enfrentar o animal")
    print("(3) Tentar fugir")
    print("(4) Ver mochila")
    print("(5) Ver noites passadas")
    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🐾 Você continua se escondendo e o animal vai embora. +5 pontos.")
            pontuacao += 5
            break

        elif escolha == "2":
            print("\n🐻 Você enfrenta o animal mas percebe que não é capaz de vencer de um urso! GAME OVER")
            vida = 0
            energia = 0
            break

        elif escolha == "3":
            print("\n🏃 Você consegue fugir, mas se cansa. +10 pontos, -20 de energia.")
            pontos += 10
            energia -= 20
            break
        elif escolha == "4":
            ver_mochila()
        elif escolha == "5":
            ver_noites()
        else:
            print("\nOpção inválida. Tente novamente.")
    verificar_game_over()
    verificar_vitoria()
    input("Pressione ENTER para ver seus status e continuar sua jornada...\n")
    
def nona_escolha():
    global vida, energia, pontuacao, mochila

    print("Você perde a noção do tempo e olha para o céu!")
    print("O sol está se pondo e você precisa decidir o que fazer a seguir.")
    print("Você tem algumas opções:\n")
    print("(1) Passar a noite na casa abandonada")
    print("(2) Voltar para a estrada e caminhar até amanhecer")
    print("(3) Seguir sua intuição e explorar a floresta à noite")
    print("(4) Ver mochila")   
    print("(5) Ver noites passadas")
    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n🌙 Você passa a noite na casa abandonada. +20 pontos, +30 de energia.")
            pontuacao += 20
            energia += 30
            break

        elif escolha == "2":
            print("\n🚗 Um carro passa pela estrada e te vê! Você consegue fugir da floresta. VICTORY")
            pontuacao = 100
            
        elif escolha == "3":
            print("\n🌲 Você se aventura na floresta à noite. QUE CORAGEM. +20 pontos, -15 de energia.")
            print("🌟 Você encontra frutas brilhantes. (+1 item na mochila)")
            print("A exaustão está clara e você cai no sono.")
            pontuacao += 20
            energia -= 15
            if len(mochila) < MOCHILA_LIMITE:
                    mochila.append("Frutas Brilhantes")
            else:
                print("Mochila cheia! Não foi possível guardar as frutas.")
            break

        elif escolha == "4":
            ver_mochila()

        elif escolha == "5":
            ver_noites()

        else:
            print("\nOpção inválida. Tente novamente.")
        
        verificar_game_over()
        verificar_vitoria()
        input("Pressione ENTER para ver seus status e continuar sua jornada...\n")


def decima_escolha():
    global vida, energia, pontuacao, mochila

    noites.append("Noites na floresta")
    print("Você acorda com o sol nascendo e sente que está perto de encontrar a saída.")
    print("Há um rio próximo.")
    print("Você tem algumas opções:\n")
    print("(1) Aproveitar o rio para se refrescar e recuperar energia")
    print("(2) Tentar pescar algo para comer")
    print("(3) Construir uma jangada para seguir o rio")
    print("(4) Ver mochila")
    print("(5) Ver noites passadas")

    while True:
        escolha = input("Digite o número da ação escolhida: ")

        if escolha == "1":
            print("\n💧 Você se refresca no rio. +20 de energia, +10 de vida.")
            energia = min(ENERGIA_MAXIMA, energia + 20)
            vida = min(VIDA_MAXIMA, vida + 10)
            break

        elif escolha == "2":
            print("\n🎣 Ótima pescaria. +10 pontos. (+1 item na mochila)")
            pontuacao += 10
            if len(mochila) < MOCHILA_LIMITE:
                mochila.append("Peixe Fresco")
            else:
                print("Mochila cheia! Não foi possível guardar o peixe.")

            break

        elif escolha == "3":
            print("\n🚣 Você não encontra recursos suficientes para contruir uma jangada. -10 de energia")
            energia -= 10
            break

        elif escolha == "4":
            ver_mochila()

        elif escolha == "5":
            ver_noites()

        else:
            print("\nOpção inválida. Tente novamente.")

        verificar_game_over()
        verificar_vitoria()
        input("Pressione ENTER para ver seus status e continuar sua jornada...\n")


   






# Execução do jogo
introducao()
primeira_escolha()
mostrar_status()
segunda_escolha()
mostrar_status()
terceira_escolha()      
mostrar_status()
quarta_escolha()
mostrar_status
quinta_escolha()
mostrar_status()
sexta_escolha()
mostrar_status()
setima_escolha()
mostrar_status()
oitava_escolha()
mostrar_status()
nona_escolha()
mostrar_status()
decima_escolha()
mostrar_status()