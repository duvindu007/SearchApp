import json
from App.model import User, Tickets , Organizations
import itertools
import logging


class Process:

    @staticmethod
    def convert_dict(lst):
        dictionary_lst= []
        for obj in lst:
            dictionary = obj.__dict__
            dictionary_lst.append(dictionary)
        return dictionary_lst

    @staticmethod
    def search(term,lst_dic,value):
       item =  [element for element in lst_dic if element[term] ==value]
       return item

    @staticmethod
    def read_json():
        with open('readable.json') as json_file:
            data = dict(json.loads(json_file.read()))
        return data

    @staticmethod
    def search_user( term , value):
        result=[]
        usrdict = Process.convert_dict(User.read_file_user())
        usr_lst=Process.search(term,usrdict,value)

        for user in usr_lst:
            result.append(User(**user))

        return result

    @staticmethod
    def search_ticket(term,value):
       result =[]
       tickdict = Process.convert_dict(Tickets.read_file_tickets())
       tick_lst = Process.search(term, tickdict, value)

       for ticket in tick_lst:
           result.append(Tickets(**ticket))

       return result

    @staticmethod
    def search_organizations(term,value):
        result =[]
        organizationsdict = Process.convert_dict(Organizations.read_file_Orgz())
        organizations_lst = Process.search(term, organizationsdict, value)

        for organization in organizations_lst:
            result.append(Organizations(**organization))

        return result

    @staticmethod
    def check(value):
        if (value.isnumeric()):
            return int(value)
        if(isinstance(value,str)):
            return value
        if(isinstance(value,list)):
            return list()




