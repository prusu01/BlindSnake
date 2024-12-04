def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        width, height = map(int, lines[0].strip().split())
        commands = lines[1].strip().split()
    return width, height, commands

def initialize_grid(width, height):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    start_x = width // 2
    start_y = height // 2
    return grid, start_x, start_y

def process_commands(grid, start_x, start_y, commands):
    width = len(grid[0])
    height = len(grid)
    x, y = start_x, start_y
    path = [(x, y)]
    grid[y][x] = 1  # Mark the starting square as visited
    moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    
    for cmd in commands:
        dx, dy = moves.get(cmd.upper(), (0, 0))
        x += dx
        y += dy
        # Wrap around the grid boundaries to simulate a torus
        x %= width
        y %= height
        grid[y][x] = 1
        path.append((x, y))
    return path

import matplotlib.pyplot as plt

def draw_grid_with_arrows(grid, path):
    height = len(grid)
    width = len(grid[0])
    fig, ax = plt.subplots(figsize=(width/2, height/2))
    
    # Draw the grid lines
    for x in range(width + 1):
        ax.axvline(x, color='gray', linewidth=0.5)
    for y in range(height + 1):
        ax.axhline(y, color='gray', linewidth=0.5)
    
    # Highlight visited squares
    for x, y in path:
        display_y = height - y - 1
        rect = plt.Rectangle((x, display_y), 1, 1, color='lightgreen')
        ax.add_patch(rect)
    
    # Draw arrows to indicate movement direction
    for i in range(len(path) - 1):
        x_start, y_start = path[i]
        x_end, y_end = path[i + 1]
        # Adjust coordinates for display
        x_start_disp = x_start + 0.5
        y_start_disp = height - y_start - 0.5
        x_end_disp = x_end + 0.5
        y_end_disp = height - y_end - 0.5
        
        dx = x_end_disp - x_start_disp
        dy = y_end_disp - y_start_disp
        
        # Handle wrapping for arrow drawing
        if abs(dx) > width / 2:
            dx -= width * (1 if dx > 0 else -1)
        if abs(dy) > height / 2:
            dy -= height * (1 if dy > 0 else -1)
        
        ax.arrow(x_start_disp, y_start_disp, dx, dy,
                 head_width=0.2, length_includes_head=True, color='red')
    
    # Set the limits and aspect ratio
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    plt.axis('off')  # Hide the axes
    plt.tight_layout()
    # plt.show()
    plt.savefig("img.png")

def main():
    file_path = 'commands.txt'  # Replace with your file path
    width, height, commands = read_input(file_path)
    grid, start_x, start_y = initialize_grid(width, height)
    path = process_commands(grid, start_x, start_y, commands)
    draw_grid_with_arrows(grid, path)

if __name__ == '__main__':
    main()
