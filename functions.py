##FUNCAO RESPONSAVEL POR CRIAR OS CAMPOS DE BATALHA DOS JOGADORES
def makeMatriz(casas):
    matriz = []
    for i in range(casas):
        matriz.append(['0 '] * casas)
    return matriz

##FUNCAO RESPONSAVEL POR IMPRIMIR OS CAMPOS DE BATALHA DOS JOGADORES
def printTab(matriz1, matriz2, sizeMatriz, vezes):
    print()
    if len(vezes) > 0:
        print(vezes[0] + (" " * ((sizeMatriz * 2) + 8 - len(vezes[0]))) + "|     " + vezes[1])
    print("    " + " ".join([chr(65 + l) for l in range(sizeMatriz)]) + (" " * 5) + ("|") + (" " * 9) + " ".join([chr(65 + l) for l in range(sizeMatriz)]))
    x = 1
    for line in zip(matriz1, matriz2):
        if x < 10:
            print(str(x) + "   " + "".join(line[0]) + (" " * 4) + ("|") + (" " * 5) + str(x) + "   " + "".join(line[1]))
        else:
            print(str(x) + "  " + "".join(line[0]) + (" " * 4) + ("|") + (" " * 5) + str(x) + "  " + "".join(line[1]))
        x += 1
    print()

##FUNCAO PARA DIFERIR A IMPRESSAO DOS CAMPOS DE BATALHA DURANTE O MOMENTO DE POSICIONA-LOS
def printTabPosi(players, sizeMatriz, player):
    print()
    print(player)
    print("    " + " ".join([chr(65 + l) for l in range(sizeMatriz)]) + (" " * 5))
    x = 1
    for line in players[player]:
        if x < 10:
            print(str(x) + "   " + "".join(line) + (" " * 4))
        else:
            print(str(x) + "  " + "".join(line) + (" " * 4))
        x += 1
    print()

##FUNCAO RESPONSAVEL POR POSICIONAR OS BARCOS DE ACORDO COM AS COORDENADAS FORNECIDAS
def boatPosition(position, players, player, embarSize, embarcations, embarPlayers):
    UPPER = 65
    col = ord(position[0]) - UPPER
    # try:
    if position[2] == "LESTE":
        for blocks in range(embarSize[str(embarcations)]):
            players[str(player)][int(position[1]) - 1][col + int(blocks)] = '1 '
            embarPlayers[embarcations][blocks] = [(int(position[1]) - 1), (col + blocks)]
    elif position[2] == "SUL":
        for blocks in range(embarSize[str(embarcations)]):
            players[str(player)][int(blocks) + (int(position[1]) - 1)][int(col)] = '1 '
            embarPlayers[embarcations][blocks] = [(int(position[1]) - 1 + blocks), (col)]
    return players
    # except IndexError:
    #     return False

##FUNCAO RESPONSAVEL POR NOMEAR OS JOGADORES E LHES FORNECER A MATRIZ DO CAMPO DE BATALHA
def namePlayers(players, matriz1, matriz2, vezes):
    # print()
    print('{:^121}'.format("NOMES DOS JOGADORES"))
    for elem in ['primeiro', 'segundo']:
        jog = input("Digite o nome do %s jogador: " % elem).upper()
        if elem == 'primeiro': 
            players[jog] = matriz1
        else:
            players[jog] = matriz2
        vezes.append(jog)
    print()
    return players

##FUNCAO RESPONSAVEL POR CONFERIR SE A POSICAO FORNECIDA PELO JOGADOR EH VALIDA
def verifyPosition(position, players, player, embarSize, embarcacao):
    UPPER = 65
    coluna = ord(position[0]) - UPPER
    if position[2] == "LESTE":
        try:
            for index in range(embarSize[str(embarcacao)]):
                if players[str(player)][int(position[1]) - 1][coluna + index] == '1 ':
                    return False
                else:
                    pass
        except ValueError:
            return False
        except IndexError:
            return False
    elif position[2] == "SUL":
        try:
            for index in range(embarSize[str(embarcacao)]):
                if players[str(player)][index + int(position[1]) - 1][coluna] == '1 ':
                    return False
                else:
                    pass
        except ValueError:
            return False
        except IndexError:
            return False
    return True

##FUNCAO RESPONSAVEL POR RETORNAR SE O JOGO TERMINOU
def endGame(matriz):
    soma = 0
    for li in matriz:
        for elem in li:
            if elem == '@ ':
                soma += 0
            elif elem == 'X ':
                soma += 0
            else:
                soma += int(elem)
    if soma != 0:
        return False
    else:
        return True

##FUNCAO RESPONSAVEL POR LANCAR A BOMBA E CONFERIR SE ELA ATINGIU ALGUMA EMBARCACAO
def olha_aBommmba(coord, players, vez, inicial, embarPlayers, init1, init2, sizeMatriz, vezes):
    UPPER = 65
    col = ord(coord[0]) - UPPER
    if players[vez][int(coord[1]) - 1][col] == 'X ' or players[vez][int(coord[1]) - 1][col] == '@ ':
        return False
    else:
        try:
            players[vez][int(coord[1]) - 1][col] == players[vez][int(coord[1]) - 1][col]
        except ValueError:
            return False
        try:
            if players[vez][int(coord[1]) - 1][col] == '0 ':
                players[vez][int(coord[1]) - 1][col] = '@ '
                inicial[int(coord[1]) - 1][col] = '@ '
                printTab(init1, init2, sizeMatriz, vezes)
                print("EROOOOOOOUU!\nNao foi dessa vez. Espere sua vez e tente novamente")
            elif players[vez][int(coord[1]) - 1][col] == '1 ':
                players[vez][int(coord[1]) - 1][col] = 'X '
                inicial[int(coord[1]) - 1][col] = 'X '
                printTab(init1, init2, sizeMatriz, vezes)
                afundou(players, embarPlayers, vez)
            return players
        except IndexError:
            return False

##FUNCAO PARA RETORNAR SE A EMBARCACAO FOI NAUFRAGADA
def afundou(players, embarPlayers, vez):
    aux = ' '
    for embar in embarPlayers:
        for posi in embarPlayers[embar]:
            if players[vez][posi[0]][posi[1]] == 'X ':
                aux = embar
            else:
                print('ACERTOOOOOOOUU!\nParabens voce atingiu a embarcacao! Seja esperto e afunde-a')
                return False
        break
    print('AFUNDOOOOOOOUU o %s!\nParabens' % aux)
    del(embarPlayers[aux])
    return True