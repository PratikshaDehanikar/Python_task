# pyramid pattern

def print_pyramid(n):
    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        print()

# Number of levels in the pyramid
n = 5
print_pyramid(n)