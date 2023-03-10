from model.Notebook_model import Notebook
from random import randint

from source.Char_source import Char_Source


class Notebooks_DB:
    @staticmethod
    def get_notebook_set():
        notebooks = []
        Notebook.set_criteria_dict()
        Notebook.set_characteristics_dict()

        for i in range(0, 100):
            brand = Char_Source.brands[randint(0, len(Char_Source.brands)-1)]
            ram = Char_Source.rams[randint(0, len(Char_Source.rams)-1)]
            hardDriveCap = Char_Source.roms[randint(0, len(Char_Source.roms)-1)]
            proc = Char_Source.procs[randint(0, len(Char_Source.procs)-1)]
            screen_diag = Char_Source.screen_diags[randint(0, len(Char_Source.screen_diags)-1)]
            os = Char_Source.oss[randint(0, len(Char_Source.oss)-1)]
            colour = Char_Source.colours[randint(0, len(Char_Source.colours)-1)]
            inStock = Char_Source.in_stocks[randint(0, len(Char_Source.in_stocks)-1)]
            price = randint(0, 100_000)
            newNotebook = Notebook(i + 1, brand, ram, hardDriveCap, proc,
                                   screen_diag, os, colour, inStock, price)
            notebooks.append(newNotebook)

        return notebooks