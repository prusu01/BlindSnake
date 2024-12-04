import random
import math
import matplotlib.pyplot as plt
import numpy

def read_commands(file_path='commands.txt'):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # Ignore the first line (grid dimensions placeholder)
        commands = lines[1:]
        # Replace all occurrences of "RIGHT" with "R"
        commands = [command.replace("RIGHT", "R").strip() for command in commands]
        commands = [command.replace("DOWN", "D").strip() for command in commands]
        

    # print(commands[0:100])
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
        # print(total_cells, cells_visited, steps, x, y)
        steps += 1
        if (x, y) not in visited:
            visited.add((x, y))
            cells_visited += 1
        if cells_visited == total_cells:
                all_cells_visited_step = steps
                break  # All cells have been visited

    return all_cells_visited_step if all_cells_visited_step is not None else steps

def generate_grid_dimensions(num_areas, num_grids_per_area, min_area=1, max_area=10000):
    # Generate unique grid areas
    areas = numpy.arange(min_area, max_area, (max_area - min_area) // num_areas)
    # areas = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    area_dimensions = {}

    for area in areas:
        dimensions_list = []

        # 1 x S
        dimensions_list.append({'area': area, 'width': 1, 'height': area})

        # S x 1
        dimensions_list.append({'area': area, 'width': area, 'height': 1})

        # Approximate sqrt(S) x sqrt(S)
        
        dimensions_list.append({'area': area, 'width': int(math.sqrt(area)), 'height': int(math.sqrt(area))})

        # 3 x (S/3)
        if area % 3 == 0 and area >= 3:
            width = 3
            height = area // 3
            dimensions_list.append({'area': area, 'width': width, 'height': height})

            # (S/3) x 3
            width = area // 3
            height = 3
            dimensions_list.append({'area': area, 'width': width, 'height': height})

        # Ensure we have exactly num_grids_per_area grids per area
        # If we have less than required, find other factor pairs
        while len(dimensions_list) < num_grids_per_area:
            possible_dimensions = []
            for w in range(1, area + 1):
                if area % w == 0:
                    h = area // w
                    possible_dimensions.append({'area': area, 'width': w, 'height': h})
            # Remove already added dimensions
            existing_dims = {(d['width'], d['height']) for d in dimensions_list}
            possible_dimensions = [d for d in possible_dimensions if (d['width'], d['height']) not in existing_dims]
            if not possible_dimensions:
                break  # No more unique dimensions
            # Randomly select additional dimensions to make up to required number
            additional_needed = num_grids_per_area - len(dimensions_list)
            additional_dimensions = random.sample(possible_dimensions, min(additional_needed, len(possible_dimensions)))
            dimensions_list.extend(additional_dimensions)

        # Take only the required number of dimensions
        dimensions_list = dimensions_list[:num_grids_per_area]
        # print(dimensions_list)

        area_dimensions[area] = dimensions_list

    return area_dimensions

def run_simulations(commands, area_dimensions):
    area_results = []
    i=0
    for area, grids in area_dimensions.items():
        i+=1
        print("running simulation for area number ", i)    

        steps_list = []
        for grid in grids:
            width = grid['width']
            height = grid['height']
            steps_taken = simulate_snake(width, height, commands)
            steps_list.append(steps_taken)
        average_steps = sum(steps_list) / len(steps_list)
        max_steps = max(steps_list)
        area_results.append({'area': area, 'average_steps': average_steps, 'max_steps': max_steps})

    return area_results

def plot_results(area_results):
    areas = [result['area'] for result in area_results]
    average_steps = [result['average_steps'] for result in area_results]
    max_steps = [result['max_steps'] for result in area_results]
    plt.figure(figsize=(10, 6))

    # Plot average steps
    plt.scatter(areas, average_steps, label='Average Steps', color='blue', alpha=0.7)

    # Plot maximum steps
    plt.scatter(areas, max_steps, label='Maximum Steps', color='red', alpha=0.7)

    # Plot y = 35x line
    max_area = max(areas)
    min_area = min(areas)
    x_line = range(min_area-1, max_area + 1)
    y_line = [35 * x for x in x_line]
    yx_line = [x for x in x_line]
    plt.plot(x_line, y_line, label='y = 35*S', color='green')
    plt.plot(x_line, yx_line, label='y = S', color='black')
    plt.title('Number of Steps to Cover the Grid vs Grid Area')
    plt.xlabel('Grid Area (number of cells)')
    plt.ylabel('Number of Steps Taken')
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig("plot.png")
a=0
def main():

    num_areas = int(input("Enter the number of areas: "))
    min_area = int(input("Enter the minimum area: "))
    max_area = int(input("Enter the maximum area: "))
    num_grids_per_area = 6
    commands = read_commands('commands.txt')
    area_dimensions = generate_grid_dimensions(num_areas, 
                                               num_grids_per_area, 
                                               min_area=min_area,
                                             max_area=max_area)
    area_results = run_simulations(commands, area_dimensions)
    plot_results(area_results)

    # Optionally, print the results
    for result in area_results:
        print(f"Area {result['area']}: Max steps taken to cover the grid = {result['max_steps']:.2f}")

    print("\n\nfinished, see the plot.png file for the results\n\n")

if __name__ == '__main__':
    main()
