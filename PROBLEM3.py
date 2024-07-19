def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def right_angle_triangle_of_ones(x):
    for y in range(1, x + 1):
        print('1 ' * y)

def palindromic_triangle(x):
    for y in range(1, x + 1):

        print(' ' * (x - y), end='')

        for w in range(1, y + 1):
            print(y, end='')

        for w in range(y - 1, 0, -1):
            print(w, end='')
        print()

def help_menu():
    print("Help:")
    print("1. Display a right-angle triangle of ones: Displays a triangle with 1s in a right-angle triangle form.")
    print("2. Display a Palindromic Triangle: Displays a triangle with numbers forming a palindrome in each row.")
    print("3. Help: Displays this help menu.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            n = int(input("Enter the number of rows: "))
            right_angle_triangle_of_ones(n)
        elif choice == '2':
            n = int(input("Enter the number of rows: "))
            palindromic_triangle(n)
        elif choice == '3':
            help_menu()
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
