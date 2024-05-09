import random


class BoardOutException(Exception):
    pass


class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, length: int, point_ship_head: Dot, direction: bool, health_points: int):
        self.head = point_ship_head
        self.length = length
        self.direction = direction  # если True то вертикально
        self.health_points = health_points

    def dots(self):
        result = [self.head]
        counter = 1
        for _ in range(self.length - 1):
            if self.direction:
                result.append(Dot(self.head.x, self.head.y + counter))
            else:
                result.append(Dot(self.head.x + counter, self.head.y))
            counter += 1
        return result


class Board:
    def __init__(self, ships: list[Ship], hid: bool, alive_ships_number: int):
        self._board = [['.'] * 6 for _ in range(6)]
        self.ships = ships
        self.hid = hid
        self.alive_ships_number = alive_ships_number

    def add_ship(self):
        for i in self.ships:
            for j in i.dots():
                if i.direction:
                    try:
                        if self._board[j.x][j.y + len(i.dots())] == '.':
                            for j in i.dots():
                                if self._board[j.x][j.y] == '.':
                                    self._board[j.x][j.y] = i
                            break
                    except IndexError:
                        print('По такому индексу поставить корабль не получается')
                        break
                else:
                    try:
                        if self._board[j.x + len(i.dots())][j.y] == '.':
                            for j in i.dots():
                                if self._board[j.x][j.y] == '.':
                                    self._board[j.x][j.y] = i
                            break
                    except IndexError:
                        print('По такому индексу поставить корабль не получается')
                        break
            self.contour()

    def contour(self):
        list_ships = []
        for i in self._board:
            for j in i:
                if isinstance(j, Ship):
                    list_ships.append(j)
        # Обходим каждую точку "x" и обводим их буквами "y"
        for i in list_ships:
            for x_and_y in i.dots():  # x_row, x_col
                # Определяем границы для обводки точки "x" буквами "y"
                min_row = max(0, x_and_y.x - 1)
                max_row = min(len(self._board) - 1, x_and_y.x + 1)
                min_col = max(0, x_and_y.y - 1)
                max_col = min(len(self._board[0]) - 1, x_and_y.y + 1)

                # Обводим точку "x" буквами "y" в пределах указанных границ
                for row in range(min_row, max_row + 1):
                    for col in range(min_col, max_col + 1):
                        if self._board[row][col] == '.':
                            self._board[row][col] = '-'

        return self._board

    def print_board(self):
        print("  0 1 2 3 4 5")
        result = self._board.copy()
        for x in range(len(result)):
            for y in range(len(result[0])):
                if isinstance(result[x][y], Ship):
                    result[x][y] = 'S'

        counter = 0
        for i in result:
            print(f'{counter} {" ".join(i)}')
            counter += 1

    def out(self, dot: Dot):
        try:
            self._board[dot.x][dot.y]
        except IndexError:
            return True
        else:
            return False

    def shot(self, dot: Dot):
        try:
            if self._board[dot.x][dot.y] == 'T' or self._board[dot.x][dot.y] == 'X':
                print('Зачем ты снова сюда стреляешь!?')
        except IndexError:
            print('Попытка выстрела за пределы доски! Повторите попытку')
        else:
            if self._board[dot.x][dot.y] == '.' or self._board[dot.x][dot.y] == '-':
                self._board[dot.x][dot.y] = 'T'
            else:
                self._board[dot.x][dot.y] = 'X'
                return True


class Player:
    def __init__(self, board_player=None):
        self._board = Board(ships_user, False, len(ships_user))
        self.enemy_board = Board(ships_ai, False, len(ships_ai))

    def ask(self):
        pass

    def move(self):
        return self.enemy_board.shot(self.ask())

    @classmethod
    def _check_for_winner(cls, board):
        merged = [x for i in board._board for x in i]
        if 'S' not in merged:
            print(merged)
            return True
        print(merged)
        return False


class User(Player):
    def ask(self):
        return Dot(int(input('В какую клетку делаем выстрел? по X: ')),
                   int(input('В какую клетку делаем выстрел? по Y: ')))


class Ai(Player):
    def ask(self):
        return Dot(random.randint(0, 5), random.randint(0, 5))


class Game:
    def __init__(self, user=None, board_user=None, ai_player=None, ai_player_board=None):
        self.user = user
        self.board_user = board_user
        self.ai = ai_player
        self.ai_player_board = ai_player_board

    def random_board(self):
        ships = []
        counter = 0
        stop_iter = 0

        while stop_iter < 100000:
            ships.append(Ship(3, Dot(random.randint(0, 5), random.randint(0, 5)), random.choice([True, False]), 3))
            ships.append(Ship(2, Dot(random.randint(0, 5), random.randint(0, 5)), random.choice([True, False]), 2))
            ships.append(Ship(2, Dot(random.randint(0, 5), random.randint(0, 5)), random.choice([True, False]), 2))
            for i in range(4):
                ships.append(Ship(1, Dot(random.randint(0, 5), random.randint(0, 5)), random.choice([True, False]), 1))

            random_board = Board(ships, False, len(ships))
            random_board.add_ship()

            for i in random_board._board:
                for j in i:
                    if isinstance(j, Ship):
                        counter += 1
            random_board.print_board()
            if counter == 10:
                break

            stop_iter += 1
            print(stop_iter)
            ships = []
            counter = 0
        return random_board

    def loop(self):
        pass

    def start(self):
        pass

    def greet(self):
        pass


ship1 = Ship(3, Dot(0, 2), True, 3)
ship2 = Ship(2, Dot(2, 2), False, 2)
ship4 = Ship(1, Dot(5, 2), False, 1)
ship5 = Ship(1, Dot(5, 5), False, 1)

ship_ai1 = Ship(3, Dot(0, 2), True, 3)
ship_ai2 = Ship(2, Dot(2, 2), True, 2)
ship_ai3 = Ship(1, Dot(4, 4), True, 1)

ships_ai = [ship_ai1, ship_ai2, ship_ai3]
ships_user = [ship2, ship4, ship5, ship1]

# b = Board(ships, False, len(ships))
# b.add_ship()
# print(b.print_board())

# b.print_board()
# user = User()
# user.enemy_board.add_ship()
#
# ai = Ai()
# ai._board.add_ship()
#
game = Game()
sh = game.random_board()
# sh.add_ship()
sh.print_board()
for i in sh._board:
    print(i)
# board = Board(sh, False, len(sh))
# print(board.add_ship())
# print(board.print_board())
# user.move()

# for i in user.enemy_board.print_board():
#     if 'S' in i:
#         print('ok')

# for i in b.print_board():
#     print(' '.join(i))
