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
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"], ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # меняем местами

    # отмена хода
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.EndRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    ''' Все возможные ходы с учето проверок'''

    def getValidMoves(self):
        return self.getAllPossibleMoves()

    ''' Все возможные ходы без учета проверок'''

    def getAllPossibleMoves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):  # Номер колонки в полученной строке
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        return moves

    # получить все возможные ходы для пешки и добавить эти действие в список
    def getPawnMoves(self, r, c, moves):
        pass

    # получить все возможные ходы для ладьи и добавить эти действие в список
    def getRookMoves(self, r, c, moves):
        pass


class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    '''Переопределяем метод equals '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return  False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]