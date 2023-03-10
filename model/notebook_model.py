from source.Char_source import Char_Source


class Notebook:
    __id = None
    __brand = ''
    __ram = 0
    __rom = 0
    __proc = ''
    __screen_diag = 0.0
    __os = ''
    __colour = ''
    __price = 0
    __in_stock = False
    __criteria_dict = {}
    __characteristics_dict = {}

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        self.__ram = ram

    def get_rom(self):
        return self.__rom

    def set_rom(self, rom):
        self.__rom = rom

    def get_proc(self):
        return self.__proc

    def set_proc(self, proc):
        self.__proc = proc

    def get_screen_diag(self):
        return self.__screen_diag

    def set_screen_diag(self, screen_diag):
        self.__screen_diag = screen_diag

    def get_os(self):
        return self.__os

    def set_os(self, os):
        self.__os = os

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_in_stock(self):
        return self.__in_stock

    def set_in_stock(self, in_stock):
        self.__in_stock = in_stock

    @staticmethod
    def get_criteria_dict():
        return Notebook.__criteria_dict

    @staticmethod
    def set_criteria_dict():
        criteria_dict = {}
        for i in range(len(Char_Source.criteria)):
            criteria_dict[i + 1] = Char_Source.criteria[i]
        Notebook.__criteria_dict = criteria_dict.copy()

    @staticmethod
    def get_characteristics_dict():
        return Notebook.__characteristics_dict

    @staticmethod
    def set_characteristics_dict():
        characteristics_dict = {}
        for crit_key in Notebook.__criteria_dict.keys():
            match crit_key:
                case 1:
                    j = len(Char_Source.brands)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.brands[j - 1]
                        j -= 1
                case 2:
                    j = len(Char_Source.rams)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.rams[j - 1]
                        j -= 1
                case 3:
                    j = len(Char_Source.roms)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.roms[j - 1]
                        j -= 1
                case 4:
                    j = len(Char_Source.procs)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.procs[j - 1]
                        j -= 1
                case 5:
                    j = len(Char_Source.screen_diags)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.screen_diags[j - 1]
                        j -= 1
                case 6:
                    j = len(Char_Source.oss)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.oss[j - 1]
                        j -= 1
                case 7:
                    j = len(Char_Source.colours)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.colours[j - 1]
                        j -= 1
                case 9:
                    j = len(Char_Source.in_stocks)
                    while j > 0:
                        characteristics_dict[f'{crit_key}{j}'] = Char_Source.in_stocks[j - 1]
                        j -= 1
        Notebook.__characteristics_dict = characteristics_dict.copy()

    def __init__(self, some_id, brand, ram, rom, proc, screen_diag, os, colour, in_stock, price):
        self.__id = some_id
        self.__brand = brand
        self.__ram = ram
        self.__rom = rom
        self.__proc = proc
        self.__screen_diag = screen_diag
        self.__os = os
        self.__colour = colour
        self.__price = price
        self.__in_stock = in_stock

    def __str__(self):
        return f"Notebook {self.__id} :\n" \
               f"\tBrand: {self.__brand}\n" \
               f"\tRAM: {self.__ram} Gb\n" \
               f"\tROM: {self.__rom} Gb\n" \
               f"\tProcessor Brand: {self.__proc}\n" \
               f"\tScreen Diagonal: {self.__screen_diag}\"\n" \
               f"\tOperating System: {self.__os}\n" \
               f"\tColour: {self.__colour}\n" \
               f"\tPrice: {self.__price}\n" \
               f"\tIn Stock: {self.__in_stock}\n"