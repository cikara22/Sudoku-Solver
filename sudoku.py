import random

# Sudoku grid dimenzii
GRID_SIZE = 9
SUBGRID_SIZE = 3

# Funkcija za proverka dali resenieto e validno
def is_valid_move(grid, row, col, num):
    # Proveri go redot
    if num in grid[row]:
        return False
    # Proveri ja kolonata
    for r in range(GRID_SIZE):
        if grid[r][col] == num:
            return False
    # Proveri gi 3x3 podtabelite
    start_row, start_col = row - row % SUBGRID_SIZE, col - col % SUBGRID_SIZE
    for r in range(start_row, start_row + SUBGRID_SIZE):
        for c in range(start_col, start_col + SUBGRID_SIZE):
            if grid[r][c] == num:
                return False
    return True

# Funkcija za display na Sudoku tabelata
def display_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Funkcija za resavanje na tabelata (backtracking algorithm)
def solve(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:  # Empty cell
                for num in range(1, GRID_SIZE + 1):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Funkcija za generiranje na sudoku zagatka 
def generate_puzzle():
    # Se zapocnuva so prazna tabela
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    # Se koristi backtracking za da se napolni tabelata vo validno Sudoku resenie
    solve(grid)
    
    # Otstrani nekoi potezi za da kreiras zagatkata 
    attempts = 50
    while attempts > 0:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if grid[row][col] != 0:
            grid[row][col] = 0
            attempts -= 1
    return grid

# funkcija za da se proveri dali zagatkata e resena
def is_solved(grid):
    for row in grid:
        if 0 in row:  # ova se prazni kelii
            return False
    return True

# Glavnata game loop
def play_sudoku():
    grid = generate_puzzle()  # Generiranje na nova zagatka
    print("Welcome to Sudoku!\n")
    
    while not is_solved(grid):
        display_grid(grid)
        
        # Zemi go vnesot na igracot
        try:
            row, col, num = map(int, input("Enter row, column, and number (1-9) separated by spaces: ").split())
            row, col = row - 1, col - 1  # prilagoduvanje na 0-baziran index
            
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and 1 <= num <= 9:
                if grid[row][col] == 0 and is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                else:
                    print("Invalid input.Try again.")
            else:
                print("Invalid input. Please make sure the numbers are within the correct range.")
        except ValueError:
            print("Invalid input format. Please enter row, column, and number (1-9) separated by spaces.")
    
    print("Congratulations! You solved the puzzle!")
    display_grid(grid)

if __name__ == "__main__":
    play_sudoku()
