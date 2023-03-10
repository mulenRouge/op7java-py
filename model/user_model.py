from model.Notebook_model import Notebook
from service.Parsers import Parsers


class User:
    __name = None
    __requested_criteria = None
    __requested_chars = None
    __filter = None

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_filter(self):
        return self.__filter

    def set_filter(self, some_filter):
        self.__filter = some_filter

    def get_requested_criteria(self):
        return self.__requested_criteria

    def set_requested_criteria(self):
        requested_criteria_dict = {}
        print("Select the criteria that you want to make the request by.")

        for i in range(1, len(Notebook.get_criteria_dict()) + 1):
            print_crit = Notebook.get_criteria_dict().get(i)
            print(f"Do you to take {print_crit} into account in your request?\nY/N: ")
            action = input()
            while True:
                if action == 'q' or action == 'Q':
                    exit(0)
                elif action == 'y' or action == 'Y':
                    if Notebook.get_criteria_dict().get(i) == "Price":
                        requested_criteria_dict[0] = "Price"
                    else:
                        requested_criteria_dict[i] = Notebook.get_criteria_dict().get(i)
                    break
                elif action == 'n' or action == 'N':
                    break
                else:
                    print("Wrong action! Try again!")
                    action = input()

        self.__requested_criteria = requested_criteria_dict.copy()

    def print_criteria(self):
        print("Your criteria list:")
        for key in self.__requested_criteria.keys():
            print(self.__requested_criteria.get(key))
        print()

    def get_requested_chars(self):
        return self.__requested_chars

    def set_requested_chars(self):
        req_chars_dict = {}
        print("Select the characteristics that you want to filter your request by.")
        for crit_key in self.__requested_criteria.keys():
            if self.__requested_criteria.get(crit_key) == "Price":
                print("What maximum price of a Notebook do you want?")
                price = input()
                while not Parsers.try_parse_int(price):
                    print("You didn't input a number! Try again!")
                    price = input()
                req_chars_dict["Price"] = price
            else:
                print(f"What {self.__requested_criteria.get(crit_key)}-s do you want to be used as a filter? Input "
                      f"one number at a time.Type 'f' to stop input the characteristics, 'q' to exit.")
                for char_key in range(1, len(Notebook.get_characteristics_dict())):
                    if not Notebook.get_characteristics_dict().get(f"{crit_key}{str(char_key)}"):
                        break
                    print(f"{Notebook.get_characteristics_dict().get(f'{crit_key}{str(char_key)}')} - {char_key}")
                while True:
                    action = input()
                    if action == 'q' or action == 'Q':
                        exit(0)
                    elif Notebook.get_characteristics_dict().get(f"{crit_key}{action}"):
                        req_chars_dict[f"{crit_key}{action}"] = \
                            Notebook.get_characteristics_dict().get(f"{crit_key}{action}")
                    elif action == 'f' or action == 'F':
                        break
                    else:
                        print("No such characteristic! Try again!")

        self.__requested_chars = req_chars_dict.copy()