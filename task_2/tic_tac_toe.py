class PlayingField:
    """
    Created tic-tac-toe fields of a certain size, change symbols by coordinates
    and check for field state
    """

    def __init__(self, field_size: int):
        """
        :param field_size: size of filed
        """
        self.size = field_size
        self.field = ["." for _ in range(field_size**2)]
        self.win_coordinates = self.calc_of_win_coordinate(size=self.size)

    @staticmethod
    def calc_of_win_coordinate(size: int) -> [list]:
        """
        :param size: size of filed
        """
        coordinates = []

        for i in range(size):

            # horiz line
            coordinates.append([i * size + n for n in range(size)])

            # vert line
            coordinates.append([n * size + i for n in range(size)])

        # left cross
        coordinates.append([n * (size + 1) for n in range(size)])

        # right cross
        coordinates.append([(size - 1) * (n + 1) for n in range(size)])

        return coordinates

    def check_field_state(self) -> str:
        # check for empty field
        if not list(filter(lambda x: x != '.', self.field)):
            return "Field is empty"

        # check for win combination
        for combination in self.win_coordinates:
            if self.field[combination[0]] == self.field[combination[1]] == self.field[combination[2]]:
                if self.field[combination[0]] != '.':
                    return f"{self.field[combination[0]]} wins!"

        return "Game is continues!"

    def make_move(self, index: int, is_cross=False):
        if is_cross:
            symb = 'X'
        else:
            symb = 'O'

        if self.field[index] == ".":
            self.field[index] = symb
        else:
            print("This point is busy!\n")
            return

        for i in range(self.size):
            start_slice = i * self.size
            end_slice = i * self.size + self.size
            print(*self.field[start_slice: end_slice])
        print("\n")

        print(self.check_field_state())


a = PlayingField(3)
a.make_move(2, is_cross=True)
a.make_move(1, is_cross=False)
a.make_move(4, is_cross=True)
a.make_move(5, is_cross=False)
a.make_move(6, is_cross=True)








