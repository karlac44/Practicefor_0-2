# Main function
def main():
    size = get_size()      # Get valid input
    print_square(size)     # Print the square

# Function to validate input
def get_size():
    while True:
        n = int(input("Enter square size (> 0): "))
        if n > 0:
            return n       # Return valid number

# Function to print a square
def print_square(size):
    for _ in range(size):          # Rows
        print("#" * size)          # Columns


main()
