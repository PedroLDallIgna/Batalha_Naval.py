from functions import *       ##IMPORTACAO DE ARQUIVO .py COM AS FUNCOES UTILIZADAS NO DESENROLAR DO PROGRAMA
from random import choice       ##IMPORTACAO DE APENAS UMA FUNCAO DE ARQUIVO .py COM FUNCOES RANDOMICAS FORNECIDAS PELA PROPRIA LINGUAGEM
from sys import exit       ##IMPORTACAO DE APENAS UMA FUNCAO DE ARQUIVO .py COM FUNCOES FORNECIDAS PELA PROPRIA LINGUAGEM

enter = input("TECLE ENTER PARA COMEÇAR O JOGO")       ##input PARA DAR INICIO AO PROGRAMA DE FATO
print()
while enter == '':       ##LOOP RESPONSAVEL POR CONTINUAR O JOGO
    print("-"*121)
    print()
    print("""O jogo de Mega Batalha Naval é uma adaptação do jogo clássico que inclui novas habilidades especiais e mais estratégia. Este jogo é jogado por 4 jogadores, cada um por si, cada um com o seu tabuleiro.

    Jogadores - 2
    Navios - Cada jogador possui 6 navios:
    1 Barco Patrulha: Tamanho: 2;
    1 Submarino: Tamanho: 3;;
    1 Destroyer: Tamanho: 3;
    1 Encouracado: Tamanho: 4; e
    1 Porta-Aviões: Tamanho: 5.
    Objetivo - Ser o último jogador a possuir algum navio não destruído""")
    print()
    print('-'*121)
    print()
    matrizSize = int(input("Digite um valor inteiro que correspondera a area de jogo (min.: 10; max.: 26): "))       ##input RESPONSAVEL POR PEDIR QUAL SERA A AREA DO CAMPO DE BATALHA DE AMBOS OS JOGADORES
    while matrizSize < 10 or matrizSize > 26:       ##LOOP RESPONSAVEL POR RESTRINGIR OS DADOS FORNECIDOS PELO JOGADOR
        matrizSize = int(input("DADO INVÁLIDO! Digite um valor inteiro que correspondera a area de jogo (min.: 10; max.: 26): "))
    matriz1 = makeMatriz(matrizSize)       ##VARIAVEL QUE ARMAZENARA O CAMPO DE BATALHA DO PRIMEIRO JOGADOR
    initialMatriz1 = makeMatriz(matrizSize)       ##VARIAVEL CORRESPONDENTE AO CAMPO DE BATALHA INICIAL DO PRIMEIRO JOGADOR
    matriz2 = makeMatriz(matrizSize)       ##VARIAVEL QUE ARMAZENARA O CAMPO DE BATALHA DO SEGUNDO JOGADOR
    initialMatriz2 = makeMatriz(matrizSize)       ##VARIAVEL CORRESPONDENTE AO CAMPO DE BATALHA INICIAL DO SEGUNDO JOGADOR
    ##VARIAVEIS PARA CADA JOGADOR QUE TEM COMO CHAVE A EMBARCACAO E COMO VALOR AS COORDENADAS REFERENTES AS SUAS POSICOES NO CAMPO DE BATALHA
    embarcacoesPlayer1 = {'Barco Patrulha':[[], []], 'Destroyer':[[], [], []], 'Submarino':[[], [], []], 'Encouracado':[[], [], [], []], 'Porta-avioes':[[], [], [], [], []]}
    embarcacoesPlayer2 = {'Barco Patrulha':[[], []], 'Destroyer':[[], [], []], 'Submarino':[[], [], []], 'Encouracado':[[], [], [], []], 'Porta-avioes':[[], [], [], [], []]}
    embarSize = {"Barco Patrulha": 2, "Destroyer": 3, "Submarino": 3, "Encouracado": 4, "Porta-avioes": 5}       ##DICIONARIO QUE CONTEM COMO CHAVE A EMBARCACAO E COMO VALOR O SEU TAMANHO
    players = {}       ##DICIONARIO QUE CONTERA OS NOMES DOS JOGADORES COMO CHAVE E SUA MATRIZ COMO VALOR
    vezes = []       ##LISTA QUE CONTERA OS NOMES DOS JOGADORES
    ##VARIAVEIS QUEBRA-GALHO (*referencias*) "DESLIGAM O FREEZER A NOTCHE"
    edmilson = initialMatriz1
    edmilson2 = embarcacoesPlayer1

    printTab(initialMatriz1, initialMatriz2, matrizSize, vezes)       ##CHAMADA DA FUNCAO PARA PRINTAR OS CAMPOS DE BATALHA
    print("-"*121)
    print()
    namePlayers(players, matriz1, matriz2, vezes)       ##CHAMADA DA FUNCAO PARA DEFINIR OS NOMES DOS JOGADORES
    printTab(initialMatriz1, initialMatriz2, matrizSize, vezes)       ##CHAMADA DA FUNCAO PARA PRINTAR OS CAMPOS DE BATALHA

    for player in players:       ##for PARA CADA UM DOS JOGADORES POSICIONAR SUAS RESPECTIVAS EMBARCACOES
        ##if E else RESPONSAVEIS POR MUDAR O VALOR DAS VARIAVEIS DE ACORDO COM O JOGADOR CORRESPONDENTE
        if player == vezes[0]:
            edmilson2 = embarcacoesPlayer1
        else:
            edmilson2 = embarcacoesPlayer2
        print()
        print("-"*121)
        print()
        print('{:^121}'.format("AGORA A VEZ EH DE %s" % player))
        ##RECOMENDACOES
        print('Forneca as coordenadas referentes para posicionar os barcos')
        print('INDIQUE A POSICAO INICIAL(COLUNA E LINHA) E A DIRECAO PARA ONDE SUA EMBARCACAO ESTARA APONTANDO')
        for embarcations in ['Barco Patrulha', 'Destroyer', 'Submarino', 'Encouracado', 'Porta-avioes']:       ##for PARA CADA UMA DAS EMBARCACOES
            ##input RESPONSAVEL POR PEDIR UMA SEQUENCIA QUE CORRESPONDERA AS COORDENADAS PARA POSICIONAR AS EMBARCACOES, EM LETRA MAIUSCULA E TRANSFORMADO EM LISTA PARA RETIRAR OS ESPACOS E ACESSAR CADA UM DOS DADOS SEPARADAMENTE
            position = str(input("Posicione o %s (Posicao Inicial(COLUNA LINHA) e Direcao, ex.:'C 9 SUL'): " % embarcations)).upper().split(" ")
            ##LOOPs PARA FAZER COM QUE OS DADOS DA VARIAVEL position ESTAO CORRETOS
            while True:
                try:
                    while position[2] != 'SUL' and position[2] != 'LESTE':
                        position = str(input("DADO INVALIDO! Posicione o %s (Posicao Inicial(COLUNA LINHA) e Direcao, ex.:'C 9 SUL'): " % embarcations)).upper().split(" ")
                    else:
                        break
                except IndexError:
                    position = str(input("DADO INVALIDO! Posicione o %s (Posicao Inicial(COLUNA LINHA) e Direcao, ex.:'C 9 SUL'): " % embarcations)).upper().split(" ")
                    try:
                        if position[2] == 'SUL' or position[2] == 'LESTE':
                            break
                    except IndexError:
                        pass
            while verifyPosition(position, players, player, embarSize, embarcations) == False:       ##CHAMADA DA FUNCAO DENTRO DE UM LOOP PARA CONFERIR SE AS CASAS PARA POSICIONAR AS EMBARCACOES ESTAO VAZIAS
                position = str(input("DADO INVALIDO! Posicione o %s (Posicao Inicial(COLUNA LINHA) e Direcao, ex.:'C 9 SUL'): " % embarcations)).upper().split(" ")       ##input PARA PEDIR NOVAMENTE AS COORDENADAS, SE ALGUMA DELAS JA ESTIVER OCUPADA
            # while boatPosition(position, players, player, embarSize, embarcations, edmilson2) == False:       ##CHAMADA DA FUNCAO DENTRO DE UM LOOP PARA POSICIONAR A EMBARCACAO
            #     position = str(input("DADO INVALIDO! Posicione o %s (Posicao Inicial(COLUNA LINHA) e Direcao, ex.:'C 9 SUL'): " % embarcations)).upper().split(" ")       ##input RESPONSAVEL POR PEDIR UMA SEQUENCIA QUE CORRESPONDERA AS COORDENADAS PARA POSICIONAR AS EMBARCACOES, EM LETRA MAIUSCULA E TRANSFORMADO EM LISTA PARA RETIRAR OS ESPACOS E ACESSAR CADA UM DOS DADOS SEPARADAMENTE
            boatPosition(position, players, player, embarSize, embarcations, edmilson2)
            printTabPosi(players, matrizSize, player)
        for i in range(40):
            print()
        printTab(initialMatriz1, initialMatriz2, matrizSize, vezes)
        # if player == vezes[0]:
        #     print()
        #     print(vezes[0])
        #     print("    " + " ".join([chr(65 + l) for l in range(matrizSize)]) + (" " * 5))
        #     x = 1
        #     for line in initialMatriz1:
        #         if x < 10:
        #             print(str(x) + "   " + "".join(line) + (" " * 4))
        #         else:
        #             print(str(x) + "  " + "".join(line) + (" " * 4))
        #         x += 1
        #     print()
        # else:
        #     print()
        #     print(vezes[1])
        #     print("    " + " ".join([chr(65 + l) for l in range(matrizSize)]) + (" " * 5))
        #     x = 1
        #     for line in initialMatriz2:
        #         if x < 10:
        #             print(str(x) + "   " + "".join(line) + (" " * 4))
        #         else:
        #             print(str(x) + "  " + "".join(line) + (" " * 4))
        #         x += 1
        #     print()

    vez = choice(vezes)       ##ESCOLHA DA VEZ DE QUEM COMECARA ATRAVES DA FUNCAO choice QUE ESCOLHE UM TERMO ALEATORIAMENTE
    print("-"*121)
    print()
    print('"CHEGOU A HORA DE SEPARARMOS OS HOMENS DOS MENINOS"\nAgora o bicho vai pegar! Forneca as coordenadas referentes para lancar as bombas no campo de batalha adversario')
    print("INDIQUE A COLUNA E A LINHA ONDE VOCE DESEJA QUE A BOMBA CAIA")
    print("LEGENDA:\nDisparo acertou a embarcacao: X\nDisparo errou a embarcacao: @")
    print("A vez do jogador que comecara sera decidida por sorteio eletronico")
    while True:
        print()
        print("-"*121)
        print()
        print('{:^121}'.format("AGORA A VEZ EH DE %s" % vez))
        ##CONDICAO PARA TROCAR O VALOR DA VARIAVEL QUEBRA-GALHO DEPENDENDO DE QUE ESTA COM A VEZ
        if vez == vezes[0]:
            edmilson = initialMatriz2
        else:
            edmilson = initialMatriz1
        bomb = str(input("Posicao em que caira a bomba(Coluna Linha; ex.: F 4): ")).upper().split(" ")       ##input RESPONSAVEL POR RECEBER AS COORDENADAS REFERENTES AO LANCAMENTO DAS BOMBAS
        ##LOOP RESPONSAVEL POR CONFERIR SE A CONDICAO DA FUNCAO E VERDADEIRA E, SE NAO, MANTER O LOOP ATE SE TORNAR VERDADEIRA
        while olha_aBommmba(bomb, players, vezes[0] if vez == vezes[1] else vezes[1], edmilson, embarcacoesPlayer2 if vez == vezes[0] else embarcacoesPlayer1, initialMatriz1, initialMatriz2, matrizSize, vezes) == False:
            bomb = str(input("DADO INVALIDO! Posicao em que caira a bomba(Coluna Linha; ex.: F 4): ")).upper().split(" ")       ##input RESPONSAVEL POR RECEBER AS COORDENADAS REFERENTES AO LANCAMENTO DAS BOMBAS
        olha_aBommmba(bomb, players, vezes[0] if vez == vezes[1] else vezes[1], edmilson, embarcacoesPlayer2 if vez == vezes[0] else embarcacoesPlayer1, initialMatriz1, initialMatriz2, matrizSize, vezes)
        ##CONDICAO PARA CONFERIR SE O JOGO TERMINOU, CHAMANDO A FUNCAO endGame()
        if endGame(matriz1) == True or endGame(matriz2) == True:
            print()
            print("-"*121)
            print("O JOGO TERMINOU")
            print("O JOGADOR %s VENCEU" % (vezes[0] if endGame(matriz2) else vezes[1]))
            printTab(matriz1, matriz2, matrizSize, vezes)
            again = str(input('Deseja jogar novamente [Y/N]? '))
            while again != 'Y' and again != 'N':
                again = str(input('DADO INVALIDO! Deseja jogar novamente [Y/N]?')).upper()
            ##CONDICAO PARA JOGAR NOVAMENTE
            if again == 'N':       ##SE NAO, A CONDICAO PARA MANTER O LOOP SE TORNARA FALSA
                print("Obrigado por jogar! Developed by: Micael S. Presotto e Pedro L. Dall' Igna")
                enter = ' '
            else:       ##SE SIM, HA UMA QUEBRA E O JOGO REINICIA
                print()
                print("-"*121)
                print()
                break
        else:
            pass
        ##CONDICAO PARA TROCAR A VEZ ENTRE OS JOGADORES
        if vez == vezes[0]:
            vez = vezes[1]
        else:
            vez = vezes[0]
else:       ##SE A CONDICAO DETERMINADA NO INICIO DO CODIGO PARA MANTER O LOOP FOR FALSA O JOGO TERMINARA
    print("Saindo...")
    exit()