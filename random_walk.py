import random

def generate_random_walk_commands(max_moves=35000000):
    commands = []
    moves_made = 0
    directions = ['U', 'D', 'L', 'R']

    while moves_made < max_moves:
        command = random.choice(directions)
        commands.append(command)
        moves_made += 1

    return commands

def write_commands_to_file(commands, file_path='commands.txt'):
    with open(file_path, 'w') as f:
        f.write("0 0\n")  # Placeholder for width and height
        f.write(' '.join(commands))

def main():
    max_moves = 35000000  # Move limit for S = 1e6
    commands = generate_random_walk_commands(max_moves)
    write_commands_to_file(commands)
    print(f"Generated {len(commands)} commands and written to 'commands.txt'.")

if __name__ == '__main__':
    main()
