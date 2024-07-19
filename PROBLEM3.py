def displayrightangletriangle(x):
    for y in range(1, x + 1):
        print(' '.join(str(num) for num in range(1, y + 1)))
    print()  

def displayrightangletriangle(x):
    for y in range(1, x + 1):
        increasing_seq = ''.join(str(num) for num in range(1, y + 1))
        decreasing_seq = ''.join(str(num) for num in range(y - 1, 0, -1))
        print(' ' * (x - y) + increasing_seq + decreasing_seq)
    print() 
    
def show_help():
    print("Menu Options:")
    print("1 - Display a right-angle triangle")
    print("2 - Display a palindromic triangle")
    print("3 - Help")
    print("4 - Exit")
    print()  

def main():
    while True:
        show_help()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            try:
                x = int(input("Enter the height of the right-angle triangle: "))
                if x <= 0:
                    raise ValueError
                displayrightangletriangle(x)
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        elif choice == '2':
            try:
                x = int(input("Enter the height of the palindromic triangle: "))
                if x <= 0:
                    raise ValueError
                displayrightangletriangle(x)
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        elif choice == '3':
            show_help()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
