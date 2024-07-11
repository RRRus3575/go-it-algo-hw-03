from colorama import Fore, Style, init

init(autoreset=True)

def hanoi(n, source, auxiliary, target, towers, moves):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        moves.append(Fore.BLUE + f"Перемістити диск з {source} на {target}: {disk}")
        moves.append(Fore.MAGENTA + f"Проміжний стан: {dict(towers)}")
        return
    hanoi(n - 1, source, target, auxiliary, towers, moves)
    disk = towers[source].pop()
    towers[target].append(disk)
    moves.append(Fore.BLUE + f"Перемістити диск з {source} на {target}: {disk}")
    moves.append(Fore.MAGENTA + f"Проміжний стан: {dict(towers)}")
    hanoi(n - 1, auxiliary, source, target, towers, moves)

def solve_hanoi(n):
    towers = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    moves = [Fore.GREEN + f"Початковий стан: {dict(towers)}"]
    hanoi(n, 'A', 'B', 'C', towers, moves)
    moves.append(Fore.GREEN + f"Кінцевий стан: {dict(towers)}")
    return moves

n = 3
moves = solve_hanoi(n)
for move in moves:
    print(move)
