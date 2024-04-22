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
        self.direction = direction
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
    def __init__(self, ships: Ship, hid: bool, alive_ships_number: int):
        self._board = [Dot(i, j) for i in range(6) for j in range(6)]
        self.ships = ships
        self.hid = hid
        self.alive_ships_number = alive_ships_number

    def add_ship(self, ship: Ship):
        pass

    def contour(self, ship):
        pass

    def print_board(self):
        pass

    def out(self, dot: Dot):
        pass

    def shot(self, dot: Dot):
        pass


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


ship = Ship(3, Dot(2, 3), False, 3)
# for i in ship.dots():
#     print(i.x, i.y)
print(ship.dots())
