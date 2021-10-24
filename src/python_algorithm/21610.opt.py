N, M = map(int, input().split())
COMMANDS = [None, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

grids = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for _ in range(M):
    j, i = map(int, input().split())
    commands, amount = COMMANDS[j], i
    clouds = [((y + commands[0] * amount) % N, (x + commands[1] * amount) % N) for y, x in clouds]
    for y, x in clouds:
        grids[y][x] += 1
    for y, x in clouds:
        grids[y][x] += sum(
            [
                grids[dy][dx] > 0
                for dx, dy in [
                    (x - 1, y - 1),
                    (x + 1, y - 1),
                    (x - 1, y + 1),
                    (x + 1, y + 1),
                ]
                if (0 <= dx < N) and (0 <= dy < N)
            ]
        )
    new_clouds = []
    for y in range(N):
        for x in range(N):
            if (y, x) not in clouds and grids[y][x] >= 2:
                new_clouds.append((y, x))
                grids[y][x] -= 2
    clouds = new_clouds

print(sum([sum(g) for g in grids]))
