from service.Parsers import Parsers
from source.Char_source import Char_Source


class Search_Service:
    __brands = []
    __rams = []
    __roms = []
    __procs = []
    __screens = []
    __oss = []
    __colours = []
    __in_stocks = []
    __max_price = 100_000_000

    def get_brands(self):
        return self.__brands

    def set_brands(self):
        self.__brands = Char_Source.brands.copy()

    def get_rams(self):
        return self.__rams

    def set_rams(self):
        self.__rams = Char_Source.rams.copy()

    def get_roms(self):
        return self.__roms

    def set_roms(self):
        self.__roms = Char_Source.roms.copy()

    def get_procs(self):
        return self.__procs

    def set_procs(self):
        self.__procs = Char_Source.procs.copy()

    def get_screens(self):
        return self.__screens

    def set_screens(self):
        self.__screens = Char_Source.screen_diags.copy()

    def get_oss(self):
        return self.__oss

    def set_oss(self):
        self.__oss = Char_Source.oss.copy()

    def get_colours(self):
        return self.__colours

    def set_colours(self):
        self.__colours = Char_Source.colours.copy()

    def get_in_stocks(self):
        return self.__in_stocks

    def set_in_stocks(self):
        self.__in_stocks = Char_Source.in_stocks.copy()

    def get_max_price(self):
        return self.__max_price

    def set_max_price(self, max_price):
        self.__max_price = max_price

    def set_user_request(self, some_filter):
        brands = []
        rams = []
        roms = []
        procs = []
        screens = []
        oss = []
        colours = []
        in_stocks = []
        max_price = 100_000_000

        for key, value in some_filter.items():
            if Parsers.try_parse_int(value) and not Parsers.try_parse_double(value):
                int_char = int(value)
                if key == "Price":
                    max_price = int_char
                elif key[0] == '2':
                    rams.append(int_char)
                elif key[0] == '3':
                    roms.append(int_char)
            else:
                if key[0] == "5":
                    screens.append(value)
                elif key[0] == '9':
                    in_stocks.append(value)
                elif key[0] == '1':
                    brands.append(value)
                elif key[0] == '4':
                    procs.append(value)
                elif key[0] == '6':
                    oss.append(value)
                elif key[0] == '7':
                    colours.append(value)

        self.__brands = brands.copy()
        self.__rams = rams.copy()
        self.__roms = roms.copy()
        self.__procs = procs.copy()
        self.__screens = screens.copy()
        self.__oss = oss.copy()
        self.__colours = colours.copy()
        self.__in_stocks = in_stocks.copy()
        self.__max_price = max_price

    def __str__(self):
        out_str = "\n"

        out_str += "Brands:\n"
        if len(self.get_brands()) == len(Char_Source.brands):
            out_str += "\tAny\n"
        else:
            for brand in self.get_brands():
                out_str += f"\t{brand}\n"

        out_str += "Rams, Gb:\n"
        if len(self.get_rams()) == len(Char_Source.rams):
            out_str += "\tAny\n"
        else:
            for ram in self.get_rams():
                out_str += f"\t{ram}\n"

        out_str += "Roms, Gb:\n"
        if len(self.get_roms()) == len(Char_Source.roms):
            out_str += "\tAny\n"
        else:
            for rom in self.get_roms():
                out_str += f"\t{rom}\n"

        out_str += "Processors:\n"
        if len(self.get_procs()) == len(Char_Source.procs):
            out_str += "\tAny\n"
        else:
            for proc in self.get_procs():
                out_str += f"\t{proc}\n"

        out_str += "Screen sizes:\n"
        if len(self.get_screens()) == len(Char_Source.screen_diags):
            out_str += "\tAny\n"
        else:
            for screen in self.get_screens():
                out_str += f"\t{screen}\"\n"

        out_str += "OS:\n"
        if len(self.get_oss()) == len(Char_Source.oss):
            out_str += "\tAny\n"
        else:
            for os in self.get_oss():
                out_str += f"\t{os}\n"

        out_str += "Colours:\n"
        if len(self.get_colours()) == len(Char_Source.colours):
            out_str += "\tAny\n"
        else:
            for colour in self.get_colours():
                out_str += f"\t{colour}\n"

        out_str += "In Stock:\n"
        if len(self.get_in_stocks()) == len(Char_Source.in_stocks):
            out_str += "\tAny\n"
        else:
            for in_stock in self.get_in_stocks():
                out_str += f"\t{in_stock}\n"

        out_str += "Max. price: "
        if self.get_max_price() == 100_000_000:
            out_str += "\tAny\n"
        else:
            out_str += f"\t{self.get_max_price()} RUB\n"

        return out_str