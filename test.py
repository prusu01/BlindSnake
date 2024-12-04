def read_commands(file_path='commands.txt'):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # Ignore the first line (grid dimensions placeholder)
        commands = lines[1].strip().split()
    return commands

def simulate_snake(grid_width, grid_height, commands):
    total_cells = grid_width * grid_height
    visited = set()
    x, y = 0, 0  # Starting position
    visited.add((x, y))
    steps = 0
    cells_visited = 1  # Start with the initial cell
    all_cells_visited_step = None

    # Movement mappings
    moves = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for command in commands:
        dx, dy = moves.get(command.upper(), (0, 0))
        x = (x + dx) % grid_width
        y = (y + dy) % grid_height
        steps += 1
        if (x, y) not in visited:
            visited.add((x, y))
            cells_visited += 1
            if cells_visited == total_cells:
                all_cells_visited_step = steps
                
                break  # All cells have been visited

    print("cells vis = ", cells_visited)
    return  steps

def test_on_grids(commands):
    grids = [
        (1, 10),
        (2, 5),
        (3, 4),
        (2, 5),
        (10, 1)
    ]

    results = []

    for width, height in grids:
        total_cells = width * height
        steps_taken = simulate_snake(width, height, commands)
        # print(total_cells, "\t\t", steps_taken)
        if steps_taken < total_cells:
            result = f"Grid {width}x{height}: Covered all cells in {steps_taken} steps."
        elif steps_taken == total_cells:
            result = f"Grid {width}x{height}: Covered all cells in exactly {steps_taken} steps."
        else:
            result = f"Grid {width}x{height}: Did not cover all cells within the commands, took {steps_taken} steps."
        results.append(result)

    return results

def main():
    commands = read_commands('commands.txt')
    results = test_on_grids(commands)
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
