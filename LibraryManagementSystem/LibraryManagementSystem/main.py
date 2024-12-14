from utils.display_menu import display_menu
from utils.clear_screen import clear_screen
from features.view_all_books import view_all_books
from features.search_book import search_book
from features.add_book import add_book
from features.check_in import checkin_book
from features.check_out import checkout_book
from features.remove_book import remove_book



def main():
    # clearing the screen when the app first starts
    clear_screen()

    while True:
        # displaying menu for navigation right after the screen is cleared
        display_menu()

        # taking user input and removing possible whitespaces
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            clear_screen()
            add_book()
        elif choice == "2":
            clear_screen()
            search_book()
        elif choice == "3":
            clear_screen()
            view_all_books()
        elif choice == "4":
            clear_screen()
            checkout_book()
        elif choice == "5":
            clear_screen()
            checkin_book()
        elif choice == "6":
            clear_screen()
            remove_book()
        elif choice == "7":
            clear_screen()
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")



# starting the program
main()
