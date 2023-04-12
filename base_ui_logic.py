def main():
    while True:
        print("""
        Calculate the mass and balance of your aircraft by choosing one of the options:
        1) Add a new aircraft
        2) Modify aircraft data
        3) Compute mass and balance
        q) Quit
        """)
        
        user_input = input("Select an option and press Enter: ")

        if user_input == "1":
            print("Add a new aircraft")

        elif user_input == "2":
            print("Modify aicraft data")

        elif user_input == "3":
            print("Compute mass and balance")

        elif user_input == "q":
            break





main()