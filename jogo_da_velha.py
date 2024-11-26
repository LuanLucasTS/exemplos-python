import random


def display_board(board):
    """Exibe o tabuleiro no console."""
    for row in board:
        print("+---" * 3 + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * 3 + "+")


def enter_move(board):
    """Obtém a jogada do usuário, valida e atualiza o tabuleiro."""
    while True:
        try:
            move = int(input("Digite sua jogada (1-9): "))
            if move < 1 or move > 9:
                print("Jogada inválida. Escolha um número entre 1 e 9.")
                continue

            # Converte o número da jogada em coordenadas do tabuleiro
            row, col = divmod(move - 1, 3)

            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 9.")


def make_list_of_free_fields(board):
    """Constrói uma lista de todas as posições livres no tabuleiro."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['X', 'O']]


def victory_for(board, sign):
    """Verifica se o jogador com o símbolo especificado venceu."""
    # Linhas, colunas e diagonais vencedoras
    winning_lines = [
        [(0, 0), (0, 1), (0, 2)],  # Linha superior
        [(1, 0), (1, 1), (1, 2)],  # Linha do meio
        [(2, 0), (2, 1), (2, 2)],  # Linha inferior
        [(0, 0), (1, 0), (2, 0)],  # Coluna esquerda
        [(0, 1), (1, 1), (2, 1)],  # Coluna do meio
        [(0, 2), (1, 2), (2, 2)],  # Coluna direita
        [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
        [(0, 2), (1, 1), (2, 0)]  # Diagonal secundária
    ]

    for line in winning_lines:
        if all(board[row][col] == sign for row, col in line):
            return True
    return False


def draw_move(board, first_move=False):
    """Realiza a jogada do computador e atualiza o tabuleiro."""
    if first_move:
        # Primeiro movimento: coloca o 'X' no meio do tabuleiro
        if board[1][1] not in ['X', 'O']:
            board[1][1] = 'X'
            return
    # Movimentos subsequentes
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = random.choice(free_fields)
        board[move[0]][move[1]] = 'X'


def main():
    """Função principal para rodar o jogo."""
    # Tabuleiro inicial
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]

    # O computador faz o primeiro movimento
    draw_move(board, first_move=True)
    display_board(board)

    while True:
        # Turno do jogador
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Você venceu! Parabéns!")
            break

        if not make_list_of_free_fields(board):
            print("Empate!")
            break

        # Turno do computador
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("O computador venceu! Tente novamente.")
            break

        if not make_list_of_free_fields(board):
            print("Empate!")
            break


if __name__ == "__main__":
    main()
