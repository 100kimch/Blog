N, M = map(int, input().split())
COMMANDS = [None, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


class Game:
    """Game class"""

    grids: list[list[int]] = []
    orders: list[tuple[int, int]] = []
    clouds: list[tuple[int, int]] = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    def __init__(self, grids: list[list[int]], orders: list[tuple[int, ...]]):
        self.grids = grids
        self.orders = [(o[0], o[1]) for o in orders]
        # print(f"cloud: {self.clouds}")
        for i in self.orders:
            # self.show_grids()
            self.move_clouds(i)
            # self.show_grids()
            self.shower()
            # self.show_grids()
            self.copy_water()
            # self.show_grids()
            self.set_clouds()

    def set_clouds(self) -> None:
        """Set new clouds"""
        new_clouds = []
        for y, grid in enumerate(self.grids):
            for x, g in enumerate(grid):
                if (y, x) not in self.clouds and g >= 2:
                    new_clouds.append((y, x))
                    self.grids[y][x] -= 2
        self.clouds = new_clouds
        # print("set new clouds")

    def move_clouds(self, order: tuple[int, int]) -> None:
        """Move the cloud"""
        commands, amount = COMMANDS[order[0]], order[1]
        self.clouds = [
            ((y + commands[0] * amount) % N, (x + commands[1] * amount) % N) for y, x in self.clouds
        ]
        # print("moved clouds")

    def shower(self) -> None:
        """Shower the cloud"""
        for y, x in self.clouds:
            self.grids[y][x] += 1
        # print("showered")

    def copy_water(self) -> None:
        """Do copy water bug"""
        for y, x in self.clouds:
            self.grids[y][x] += sum(
                [
                    self.grids[dy][dx] > 0
                    for dx, dy in [
                        (x - 1, y - 1),
                        (x + 1, y - 1),
                        (x - 1, y + 1),
                        (x + 1, y + 1),
                    ]
                    if (dx < N) and (dx >= 0) and (dy < N) and (dy >= 0)
                ]
            )
        # print("copied water")

    def show_grids(self) -> None:
        """Show current grids"""
        for y, j in enumerate(self.grids):
            for x, i in enumerate(j):
                print(f"{(str(i) + ('*' if (y, x) in self.clouds else '')):6s}", end="")
            print()

    def get_water_amount(self) -> int:
        """Get final water amount"""
        return sum([sum(g) for g in self.grids])


game = Game(
    [list(map(int, input().split())) for _ in range(N)],
    [tuple(map(int, input().split())) for _ in range(M)],
)

print(game.get_water_amount())
