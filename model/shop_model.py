from service.Search_service import Search_Service


class Shop:
    __notebooks = []
    __request = None

    @staticmethod
    def get_notebooks():
        return Shop.__notebooks
    @staticmethod
    def set_notebooks(notebooks):
        Shop.__notebooks = notebooks.copy()

    def set_request(self, some_filter):
        new_request = Search_Service()
        new_request.set_user_request(some_filter)

        if len(new_request.get_brands()) == 0:
            new_request.set_brands()
        if len(new_request.get_rams()) == 0:
            new_request.set_rams()
        if len(new_request.get_roms()) == 0:
            new_request.set_roms()
        if len(new_request.get_screens()) == 0:
            new_request.set_screens()
        if len(new_request.get_procs()) == 0:
            new_request.set_procs()
        if len(new_request.get_oss()) == 0:
            new_request.set_oss()
        if len(new_request.get_colours()) == 0:
            new_request.set_colours()
        if len(new_request.get_in_stocks()) == 0:
            new_request.set_in_stocks()
        self.__request = new_request

    def get_request(self):
        return self.__request

    def __str__(self):
        out_str = ''
        for note in self.__notebooks:
            out_str += str(note)
        return out_str