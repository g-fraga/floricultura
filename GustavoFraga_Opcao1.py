# ==============================================================
#  PROJETO FINAL - SISTEMA FLORICULTURA
#  Aluno: Gustavo Fraga
#  Opção de projeto escolhida: Opção 1 - Sistema Floricultura
#  Curso: Análise e Desenvolvimento de Sistemas
# ==============================================================

# --------------------------------------------------------------
# CATÁLOGO DO DIA
# São duas listas "paralelas": a flor da posição 0 tem o preço da
# posição 0, a flor da posição 1 tem o preço da posição 1, e assim
# por diante. Para mudar as flores ou os preços, basta editar aqui.
# --------------------------------------------------------------
flores = ["Margarida", "Rosa", "Violeta", "Orquídea"]
precos = [10, 15, 5, 50]

# Lista que guarda as flores escolhidas pelo cliente (o carrinho).
# Começa vazia e recebe um item a cada compra.
carrinho = []

# Guarda a opção escolhida no menu. Começa vazia para entrar no laço.
opcao = ""

# --------------------------------------------------------------
# LAÇO PRINCIPAL: o menu se repete até o usuário escolher F
# --------------------------------------------------------------
while opcao != "F":
    print("-" * 21)
    print(" FLORICULTURA")
    print("-" * 21)
    print("C - Comprar")
    print("R - Remover")
    print("L - Listar itens")
    print("F - Finalizar")
    print("-" * 21)

    # strip() tira espaços extras e upper() deixa em maiúscula,
    # assim "c" e "C" funcionam do mesmo jeito
    opcao = input("Digite a opção desejada: ").strip().upper()

    # ======================= C - COMPRAR =======================
    if opcao == "C":
        continuar = "S"

        # Repete enquanto o usuário quiser comprar mais flores
        while continuar == "S":
            # Mostra o catálogo percorrendo as listas com for
            print("-" * 21)
            print(" FLORICULTURA")
            print("-" * 21)
            for i in range(len(flores)):
                # i + 1 porque a lista começa no índice 0,
                # mas para o cliente o catálogo começa no 1.
                # :<9 e :>2 só completam com espaços para alinhar as colunas
                print(f"{i + 1} - {flores[i]:<9} - R${precos[i]:>2}")
            print("-" * 21)

            escolha = input("Informe a flor desejada: ").strip()

            # Validação: isdigit() confere se foi digitado um número
            # e depois conferimos se esse número existe no catálogo
            if escolha.isdigit() and int(escolha) >= 1 and int(escolha) <= len(flores):
                posicao = int(escolha) - 1
                carrinho.append(flores[posicao])  # adiciona a flor no fim da lista
                print(f"Item adicionado ao carrinho: {flores[posicao]}")
            else:
                print("Opção inválida! Nenhuma flor foi adicionada.")

            # Pergunta se quer continuar e só aceita S ou N
            continuar = input("Deseja comprar mais flores? (S/N): ").strip().upper()
            while continuar != "S" and continuar != "N":
                print("Resposta inválida! Digite S para Sim ou N para Não.")
                continuar = input("Deseja comprar mais flores? (S/N): ").strip().upper()

        # Quando a resposta for N, o laço termina e o menu aparece de novo

    # ======================= R - REMOVER =======================
    elif opcao == "R":
        if len(carrinho) == 0:
            print("Seu carrinho está vazio. Não há itens para remover.")
        else:
            # Mostra todos os itens do carrinho numerados
            for i in range(len(carrinho)):
                print(f"{i + 1} {carrinho[i]}")

            escolha = input("Informe a opção para remover: ").strip()

            # Validação: o número precisa existir na lista do carrinho
            if escolha.isdigit() and int(escolha) >= 1 and int(escolha) <= len(carrinho):
                posicao = int(escolha) - 1
                # pop() remove SOMENTE o item daquela posição.
                # Se houver duas Rosas, só a escolhida sai do carrinho.
                item_removido = carrinho.pop(posicao)
                print(f"Item removido do carrinho: {item_removido}")
            else:
                print("Opção inválida! Nenhum item foi removido.")

        # Depois da remoção, o menu aparece de novo

    # ======================= L - LISTAR ========================
    elif opcao == "L":
        if len(carrinho) == 0:
            print("Seu carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            print(carrinho)  # mostra a lista inteira, inclusive os repetidos

    # ======================= F - FINALIZAR =====================
    elif opcao == "F":
        total = 0

        if len(carrinho) == 0:
            print("Seu carrinho está vazio.")
        else:
            # Percorre o carrinho mostrando cada item e somando o preço
            for i in range(len(carrinho)):
                item = carrinho[i]
                print(f"{i + 1} {item}")
                # index() descobre em que posição a flor está na lista de flores;
                # o preço dela está nessa mesma posição na lista de preços
                posicao = flores.index(item)
                total = total + precos[posicao]

        print(f"Você deve: R${total}")
        print("Obrigado pela compra! Volte sempre.")
        print("Finalizando a compra..")
        # Como a opção agora é "F", o while termina e o programa se encerra

    # ===================== OPÇÃO INVÁLIDA ======================
    else:
        print("Opção inválida! Escolha C, R, L ou F.")
