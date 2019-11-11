import os
from App.repository import Process
import logging

logging.basicConfig(filename='log\\app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# Greeter is a terminal application that Search Tickets, Users and Organizations,

### FUNCTIONS ###
class View:
    @staticmethod
    def display_title_bar():
        # Clears the terminal screen, and displays a title bar.
        os.system('cls')
        print("\t**********************************************")
        print("\t*** 'Type 'quit' to exit at anytime, Press 'Enter' to continue'!  ***")
        print("\t**********************************************\n")

    @staticmethod
    def get_user_choice():
        # Let users know what they can do.
        print("*******************************")
        print("Press 1 to Search Zendesk.")
        print("Press 2 to view a list of searchable fields")
        print("Type 'Quit' to exit")

        return input('What would you like to do?\n')

    @staticmethod
    def searchable_fields():
        #Display searchable fields.
        dic = Process.read_json()
        print("--------", dic["Users"], "-----------")
        print("--------", dic["Tickets"], "----------")
        print("--------", dic["Organizations"], "------")

    @staticmethod
    def search_user_zendesk(term, value):
        #search user
        assigned_t_num = 0 #create a variable holds ticket count each time ticket is created
        submited_t_num = 0
        try:

            users = Process.search_user(term, value)
            if (len(users) >= 1):
                for user in users:

                    print("----------User details-------")
                    print('\n'.join("%s : %s" % item for item in vars(user).items()))
                    print('Organization name : ', Process.search_organizations("_id", user.organization_id)[0].name)
                    print("\n------Assigned Tickets-------")
                    assign_tickets = Process.search_ticket("assignee_id", user._id)
                    for ticket in assign_tickets:
                        print(f"ticket_{assigned_t_num}", ticket.description)
                        assigned_t_num = assigned_t_num + 1
                    print("\n-----Submited Tickets--------")
                    submited_tickets = Process.search_ticket("submitter_id", user._id)
                    for ticket in submited_tickets:
                        print(f"ticket_{submited_t_num}", ticket.description)
                        submited_t_num = submited_t_num + 1
            if (len(users) == 0):
                print("Sorry user does not exist")

        except KeyError:
            print("Please enter valid term and value ")
            logging.error("Key Error")

    @staticmethod
    def search_ticket_zendesk(term, value):
        try:

            tickets = Process.search_ticket(term, value)
            if (len(tickets) >= 1):
                for ticket in tickets:
                    print("--------Ticket details-----------")
                    print('\n'.join("%s : %s" % item for item in vars(ticket).items()))
                    print("---------Ticket Organization--------------")
                    print('Organization name : ', Process.search_organizations("_id", ticket.organization_id)[0].name)
                    print("--------Ticket Submitter---------")
                    submitted_user = Process.search_user("_id", ticket.submitter_id)
                    for user in submitted_user:
                        print("Submitter Name : ", user.name)
                    print("--------Assigned------------------")
                    assigned = Process.search_user("_id", ticket.assignee_id)
                    for user in assigned:
                        print("Assignee Name : ", user.name)
            if (len(tickets) == 0):
                print("Sorry , Ticket does not exist ")
        except KeyError:
            print("Please enter valid term and value ")
            logging.error("Key Error")

    @staticmethod
    def search_organization_zendesk(term, value):
        try:
            orgs = Process.search_organizations(term, value)
            if (len(orgs) >= 1):
                for organization in orgs:
                    print("--------Organization details-----------")
                    print('\n'.join("%s : %s" % item for item in vars(organization).items()))
                    print("---------Users in the Organization--------------")
                    users_orgs = Process.search_user("organization_id", organization._id)
                    for user in users_orgs:
                        print("User Name : ", user.name)
                    print("--------Tickets in Organization---------")
                    tickets_orgz = Process.search_ticket("organization_id", organization._id)
                    for ticket in tickets_orgz:
                        print("Ticket Id : ", ticket._id)
            if (len(orgs) == 0):
                print("Sorry Organization is not available")
        except KeyError:
            print("Please enter valid term and value ")
            logging.error("Key Error")


    @staticmethod
    def search_zendesk():
        # let users select search options
        print("\tSelect 1) Users 2) Tickets or 3) Organizations ")
        try:
            selected_number = int(input())
            print("please enter the search term")
            term = input()
            print("please enter the search value")
            value = input()
            if (value.isnumeric() or isinstance(value, str)):
                value = Process.check(value)

                if (selected_number == 1):
                    View.search_user_zendesk(term, value)
                elif (selected_number == 2):
                    View.search_ticket_zendesk(term, value)
                elif (selected_number == 3):
                    View.search_organization_zendesk(term, value)
                else:
                    print("Please enter valid inputs only")
            else:
                print("Please enter Numbers or Strings only")

        except ValueError:
            print("Error occurred please enter Numbers only")
            logging.error("Value Error")
