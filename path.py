import math

#Modify this function to get different configurations

def get_primes_indices(i): 
    # Example implementation
    # For demonstration, let's cycle through different window sizes based on 'i'
    # f = 4.5
    # d = 10000
    # t = 1
    # t2  = 8
    # last_index = max(2, (f - (i/1000000))) * math.log(i/d + t) + t2      # Upper bound
    # first_index = max(0, (last_index - 40))
    # return 0, int(last_index)
    # x = i
    # a = 0.00001
    # b = 0.00001
    # c = -0.0002
    # d = 0.002
    # e = 0.02
    # f = 2
    # last_index = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    # return 0, int(last_index)
    last_index = i/200000 +14
    return 0, int(last_index)


def generate_commands(max_moves=35000000):
    # Full list of primes up to a reasonable limit
    primes_pool = [
        1, 2, 3, 5, 7, 11, 13,5, 17, 19, 23,3, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
        179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
        419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
        547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
        607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
        661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
        739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
        811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
        877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
        947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
        1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063,
        1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123
    ]

    commands = []
    moves_made = 0
    i = 1  # Command index, starts from 1

    while moves_made < max_moves:
        # Call the external function with the current command index

        first_index, last_index = get_primes_indices(i)
        # print(first_index, last_index)
        # Ensure indices are within bounds
        first_index = max(0, first_index)
        last_index = min(len(primes_pool) - 1, last_index)

        # Get the current list of primes
        current_primes = primes_pool[first_index:last_index + 1]
        # print(current_primes)
        for p in current_primes:
            
            # Move right 'p' steps
            for _ in range(p):
                if moves_made >= max_moves:
                    break
                commands.append('RIGHT\n')
                moves_made += 1
                i += 1  # Increment command index

            if moves_made >= max_moves:
                break

            # Move down 1 step
            if moves_made < max_moves:
                commands.append('DOWN\n')
                moves_made += 1
                i += 1  # Increment command index
            else:
                break

        if moves_made >= max_moves:
            break

    return commands

def write_commands_to_file(commands, file_path='commands.txt'):
    with open(file_path, 'w') as f:
        f.write("0 0\n")  # Placeholder for width and height
        f.write(''.join(commands))
def main():
    max_moves = 35000000  # Move limit for S up to 1e6
    commands = generate_commands(max_moves)
    write_commands_to_file(commands)
    print(f"Generated {len(commands)} commands and written to 'commands.txt'.")

if __name__ == '__main__':
    main()