from model.Shop_model import Shop


class Search:
    __filtered_notes = []
    __request = None

    def __init__(self, request):
        self.__request = request

    def get_request(self):
        return self.__request

    def set_request(self, request):
        self.__request = request

    def get_filtered_notes(self):
        filteredNotes = []
        for brand in self.__request.get_brands():
            for ram in self.__request.get_rams():
                for rom in self.__request.get_roms():
                    for proc in self.__request.get_procs():
                        for screen in self.__request.get_screens():
                            for os in self.__request.get_oss():
                                for colour in self.__request.get_colours():
                                    for in_stock in self.__request.get_in_stocks():
                                        notes_for_search = Shop.get_notebooks().copy()
                                        for note in notes_for_search:
                                            if note.get_brand() == brand and note.get_ram() == ram \
                                                    and note.get_rom() == rom and note.get_proc() == proc \
                                                    and note.get_screen_diag() == screen and note.get_os() == os \
                                                    and note.get_colour() == colour \
                                                    and note.get_in_stock() == in_stock \
                                                    and note.get_price() <= self.get_request().get_max_price():
                                                filteredNotes.append(note)
        self.__filtered_notes = filteredNotes.copy()
        return self.__filtered_notes

    def __str__(self):
        out_str = '\n'
        notes = self.get_filtered_notes()
        if len(notes) != 0:
            out_str += "List of notebooks that fit the filter: "
            for note in notes:
                out_str += str(note)
            return out_str
        return "There are no notebooks that fit your criteria"