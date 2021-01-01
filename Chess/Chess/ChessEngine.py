"""
В этом классе мы храним все данные, поэтому этот класс отвечает за хранение всей
информации связанной с текущем состоянием шахматной ппартией. Также будет возможность
остановить ход в текущем сосотянии игры. Будет вести журнал ходов, поэтому мы сможем
отменить ходы и посмотреть как развивалась партия.
"""


class GameState():
    def __init__(self):
        """ Доска состоит из списка 8*8, где каждый элемент имеет 2 характеристики.
            Первая характеристика отвечает за цвет w-белый, b-черный.
            Вторя характеристика отвечает за тип фигуры.
            Queen - королева, King - король, Bishop - слон, K(n)ight- конь, Rook - ладья, pawn - пешка.
            "--" пустое пространство """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
