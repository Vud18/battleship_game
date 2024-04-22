class BoardOutException(Exception):
    pass


class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, point_ship_head: Dot, length: int, direction: bool, health_points: int):
        self.length = length
        self.head = point_ship_head
        self.direction = direction
        self.health_points = health_points

    def dots(self):
        pass


class Board:
    def __init__(self):
        self._board = [Dot(i, j) for i in range(6) for j in range(6)]


class Player:
    def __init__(self):
        self._board = Board()
        self.enemy_board = Board()

    def ask(self):
        pass

    def move(self):
        pass


class User(Player):
    def ask(self):
        pass


class Ai(Player):
    def ask(self):
        pass


class Game:
    def __init__(self, user, ai_player):
        self.user = user
        self.board_user = Board()
        self.ai = ai_player
        self.ai_player_board = Board()

    def random_board(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass

    def greet(self):
        pass

