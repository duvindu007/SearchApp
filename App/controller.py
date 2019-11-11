from App.view import View

def start():

    choice = ''
    View.display_title_bar()
    while choice != 'quit':
        choice = View.get_user_choice()
        # Respond to the user's choice.
        if choice == '1':
            View.search_zendesk()
        elif choice == '2':
            View.searchable_fields()
        elif choice == 'quit':
            quit()
            print("\nThanks for playing. Bye.")
        else:
            print("\nI didn't understand that choice.\n")


if __name__ == "__main__":
    #running controller function
    start()